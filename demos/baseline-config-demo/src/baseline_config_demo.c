#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEFAULT_CONFIG_PATH "/etc/justiceforme/demo-one.conf"
#define MAX_LINE 512

struct config {
    char mode[32];
    char label[96];
    int audit_enabled;
};

static void set_defaults(struct config *cfg) {
    snprintf(cfg->mode, sizeof(cfg->mode), "%s", "baseline");
    snprintf(cfg->label, sizeof(cfg->label), "%s", "JusticeForMe Demonstration One");
    cfg->audit_enabled = 1;
}

static void trim(char *s) {
    char *start = s;
    while (*start == ' ' || *start == '\t') start++;
    if (start != s) memmove(s, start, strlen(start) + 1);
    size_t n = strlen(s);
    while (n > 0 && (s[n - 1] == '\n' || s[n - 1] == '\r' || s[n - 1] == ' ' || s[n - 1] == '\t')) s[--n] = '\0';
}

static int parse_bool(const char *v, int *out) {
    if (!strcmp(v, "1") || !strcasecmp(v, "true") || !strcasecmp(v, "yes")) { *out = 1; return 0; }
    if (!strcmp(v, "0") || !strcasecmp(v, "false") || !strcasecmp(v, "no")) { *out = 0; return 0; }
    return -1;
}

static int load_config(const char *path, struct config *cfg) {
    FILE *fp = fopen(path, "r");
    if (!fp) {
        if (errno == ENOENT) return 0;
        fprintf(stderr, "cannot open %s: %s\n", path, strerror(errno));
        return -1;
    }
    char line[MAX_LINE];
    unsigned long line_no = 0;
    while (fgets(line, sizeof(line), fp)) {
        line_no++;
        trim(line);
        if (!line[0] || line[0] == '#') continue;
        char *eq = strchr(line, '=');
        if (!eq) {
            fprintf(stderr, "%s:%lu: expected key=value\n", path, line_no);
            fclose(fp);
            return -1;
        }
        *eq = '\0';
        char *key = line;
        char *value = eq + 1;
        trim(key); trim(value);
        if (!strcmp(key, "mode")) {
            snprintf(cfg->mode, sizeof(cfg->mode), "%s", value);
        } else if (!strcmp(key, "label")) {
            snprintf(cfg->label, sizeof(cfg->label), "%s", value);
        } else if (!strcmp(key, "audit_enabled")) {
            if (parse_bool(value, &cfg->audit_enabled) != 0) {
                fprintf(stderr, "%s:%lu: invalid boolean\n", path, line_no);
                fclose(fp);
                return -1;
            }
        } else {
            fprintf(stderr, "%s:%lu: unknown key '%s'\n", path, line_no, key);
            fclose(fp);
            return -1;
        }
    }
    fclose(fp);
    return 0;
}

int main(int argc, char **argv) {
    const char *path = getenv("JUSTICEFORME_DEMO_CONFIG");
    if (!path || !*path) path = DEFAULT_CONFIG_PATH;
    if (argc == 3 && !strcmp(argv[1], "--config")) path = argv[2];
    else if (argc != 1) {
        fprintf(stderr, "usage: %s [--config PATH]\n", argv[0]);
        return 64;
    }

    struct config cfg;
    set_defaults(&cfg);
    if (load_config(path, &cfg) != 0) return 78;

    printf("demo=baseline-config-demo\n");
    printf("config_path=%s\n", path);
    printf("mode=%s\n", cfg.mode);
    printf("label=%s\n", cfg.label);
    printf("audit_enabled=%s\n", cfg.audit_enabled ? "true" : "false");
    return 0;
}
