const metrics = {
  world_writable_etc: ['World-writable /etc entries', 0, 1],
  executable_files_etc: ['Executable files in /etc', 5, 20],
  privileged_binaries: ['Setuid/setgid binaries', 20, 60],
  file_capabilities: ['File capabilities', 5, 20],
  package_integrity_findings: ['Package integrity findings', 0, 10],
  recent_etc_changes_30d: ['Recent /etc changes', 25, 100]
};

const el = id => document.getElementById(id);
const severity = (value, warn, high) => value >= high ? 'high' : value > warn ? 'warn' : 'ok';

function render(report) {
  if (!report || report.schema_version !== '1.0' || !report.metrics) throw new Error('Unsupported or incomplete report schema.');
  el('host').textContent = report.host || 'unknown';
  el('generated').textContent = report.generated_at ? new Date(report.generated_at).toLocaleString() : 'unknown';
  el('rootComplete').textContent = report.root_complete ? 'Yes' : 'No — rerun with sudo';
  const cards = el('cards');
  const priorities = el('priorities');
  cards.replaceChildren(); priorities.replaceChildren();

  Object.entries(metrics).forEach(([key, [label, warn, high]]) => {
    const value = Number(report.metrics[key] ?? 0);
    const level = severity(value, warn, high);
    const card = document.createElement('article');
    card.className = `metric ${level}`;
    card.innerHTML = `<span>${label}</span><strong>${value}</strong><small>${level === 'ok' ? 'baseline review' : level === 'warn' ? 'review recommended' : 'priority review'}</small>`;
    cards.append(card);
    if (level !== 'ok') {
      const item = document.createElement('li');
      item.textContent = `${label}: ${value}. Validate ownership, package provenance, timestamps, and operational necessity.`;
      priorities.append(item);
    }
  });

  if (!priorities.children.length) priorities.innerHTML = '<li>No threshold-based priority findings. Continue baseline comparison and manual review.</li>';
  const artifacts = el('artifacts'); artifacts.replaceChildren();
  (report.artifacts || []).forEach(name => { const li = document.createElement('li'); li.textContent = name; artifacts.append(li); });
  el('notice').textContent = report.notice || 'Indicators require human review.';
  el('summary').classList.remove('hidden');
  el('status').textContent = 'Report loaded';
}

el('file').addEventListener('change', async event => {
  try { render(JSON.parse(await event.target.files[0].text())); }
  catch (error) { el('status').textContent = error.message; }
});

el('demo').addEventListener('click', () => render({
  schema_version: '1.0', generated_at: new Date().toISOString(), host: 'demonstration-host', root_complete: true,
  metrics: { world_writable_etc: 1, executable_files_etc: 7, privileged_binaries: 28, file_capabilities: 6, package_integrity_findings: 3, recent_etc_changes_30d: 42 },
  artifacts: ['etc-metadata.txt','etc-sha256.txt','privileged-binaries.txt','package-integrity.txt'],
  notice: 'Demonstration data only. Findings are not proof of malicious activity.'
}));
