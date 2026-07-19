#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
HOST="$(hostname -s 2>/dev/null || hostname)"
OUT="${1:-$PWD/justiceforme-audit-${HOST}-${STAMP}}"
mkdir -p "$OUT"

need_root=false
[[ ${EUID:-$(id -u)} -ne 0 ]] && need_root=true

safe_count() { find "$@" 2>/dev/null | wc -l | tr -d ' '; }
json_escape() { python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'; }

find /etc -xdev -printf '%y|%m|%u|%g|%s|%TY-%Tm-%TdT%TH:%TM:%TS|%p|%l\n' 2>/dev/null | sort > "$OUT/etc-metadata.txt"
find /etc -xdev -type f -print0 2>/dev/null | sort -z | xargs -0 -r sha256sum 2>/dev/null > "$OUT/etc-sha256.txt" || true
find /etc -xdev -perm -0002 -printf '%m|%u|%g|%p\n' 2>/dev/null | sort > "$OUT/etc-world-writable.txt"
find /etc -xdev -type f -perm /111 -printf '%m|%u|%g|%p\n' 2>/dev/null | sort > "$OUT/etc-executable-files.txt"
find / -xdev -type f \( -perm -4000 -o -perm -2000 \) -printf '%m|%u|%g|%p\n' 2>/dev/null | sort > "$OUT/privileged-binaries.txt"

if command -v getcap >/dev/null 2>&1; then
  getcap -r / 2>/dev/null | sort > "$OUT/file-capabilities.txt" || true
else
  : > "$OUT/file-capabilities.txt"
fi

{
  echo '# UID 0 accounts'; awk -F: '$3==0{print}' /etc/passwd
  echo; echo '# Administrative groups'
  for g in sudo wheel adm admin root docker lxd libvirt disk shadow; do getent group "$g" 2>/dev/null || true; done
  echo; echo '# Sudo configuration metadata'
  find /etc/sudoers /etc/sudoers.d -maxdepth 2 -type f -printf '%m|%u|%g|%p\n' 2>/dev/null || true
} > "$OUT/admin-access.txt"

{
  echo '# systemd local units'; find /etc/systemd/system -type f -o -type l 2>/dev/null | sort
  echo; echo '# cron'; find /etc/cron.d /etc/cron.daily /etc/cron.hourly /etc/cron.weekly /etc/cron.monthly -type f -printf '%m|%u|%g|%p\n' 2>/dev/null | sort
  echo; echo '# ld.so.preload'; [[ -f /etc/ld.so.preload ]] && cat /etc/ld.so.preload || echo 'not present'
} > "$OUT/persistence-and-loader.txt"

if command -v dpkg >/dev/null 2>&1; then
  dpkg --verify > "$OUT/package-integrity.txt" 2>&1 || true
elif command -v rpm >/dev/null 2>&1; then
  rpm -Va > "$OUT/package-integrity.txt" 2>&1 || true
elif command -v pacman >/dev/null 2>&1; then
  pacman -Qkk > "$OUT/package-integrity.txt" 2>&1 || true
else
  echo 'No supported package verifier found.' > "$OUT/package-integrity.txt"
fi

WORLD_WRITABLE=$(wc -l < "$OUT/etc-world-writable.txt" | tr -d ' ')
ETC_EXEC=$(wc -l < "$OUT/etc-executable-files.txt" | tr -d ' ')
PRIV_BIN=$(wc -l < "$OUT/privileged-binaries.txt" | tr -d ' ')
CAPS=$(wc -l < "$OUT/file-capabilities.txt" | tr -d ' ')
PKG_CHANGES=$(grep -cv '^$' "$OUT/package-integrity.txt" || true)
RECENT_ETC=$(find /etc -xdev -type f -mtime -30 2>/dev/null | wc -l | tr -d ' ')

cat > "$OUT/report.json" <<JSON
{
  "schema_version": "1.0",
  "generated_at": "$(date -u +%FT%TZ)",
  "host": "${HOST}",
  "root_complete": $([[ "$need_root" == false ]] && echo true || echo false),
  "metrics": {
    "world_writable_etc": ${WORLD_WRITABLE},
    "executable_files_etc": ${ETC_EXEC},
    "privileged_binaries": ${PRIV_BIN},
    "file_capabilities": ${CAPS},
    "package_integrity_findings": ${PKG_CHANGES},
    "recent_etc_changes_30d": ${RECENT_ETC}
  },
  "artifacts": [
    "etc-metadata.txt",
    "etc-sha256.txt",
    "etc-world-writable.txt",
    "etc-executable-files.txt",
    "privileged-binaries.txt",
    "file-capabilities.txt",
    "admin-access.txt",
    "persistence-and-loader.txt",
    "package-integrity.txt"
  ],
  "notice": "Indicators require human review and are not proof of malicious activity."
}
JSON

( cd "$OUT" && sha256sum ./* > REPORT-SHA256SUMS.txt )
printf 'Audit complete: %s\nOpen docs/index.html and load %s/report.json\n' "$OUT" "$OUT"
