from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).parents[1]
DOCS = ROOT / "docs"
REQUIRED_DOCS = [
    DOCS / "project-overview.md",
    DOCS / "architecture.md",
    DOCS / "onboarding.md",
    DOCS / "developer-guide.md",
    DOCS / "report-schema.md",
    DOCS / "security-and-evidence.md",
    DOCS / "guide.html",
    ROOT / "taskchain.md",
    ROOT / "punchlist.md",
    ROOT / "release.md",
    ROOT / "changelog.md",
]
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.lang = False
        self.main = 0
        self.h1 = 0
        self.labels = 0
        self.links: list[str] = []
        self.scripts: list[str] = []
        self.styles: list[str] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html" and values.get("lang"):
            self.lang = True
        elif tag == "main":
            self.main += 1
        elif tag == "h1":
            self.h1 += 1
        elif tag == "label":
            self.labels += 1
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag == "script" and values.get("src"):
            self.scripts.append(values["src"])
        elif tag == "link" and values.get("rel") == "stylesheet":
            self.styles.append(values.get("href", ""))


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split()[0].strip("<>")
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("mailto:", "#")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    return (source.parent / path).resolve()


def workflow_structure(text: str) -> tuple[str, list[str], list[str]]:
    trigger_section, remainder = text.split("permissions:", 1)
    uses = [line.split("uses:", 1)[1].strip() for line in text.splitlines() if line.strip().startswith("uses:")]
    permission_lines = [line.strip() for line in remainder.split("concurrency:", 1)[0].splitlines() if ":" in line]
    return trigger_section, uses, permission_lines


class DocumentationTests(unittest.TestCase):
    def test_required_documentation_exists(self):
        for path in REQUIRED_DOCS:
            self.assertTrue(path.is_file(), path)

    def test_markdown_links_resolve(self):
        sources = [ROOT / "README.md", *ROOT.glob("*.md"), *DOCS.glob("*.md")]
        for source in sources:
            text = source.read_text(encoding="utf-8")
            for match in MD_LINK.finditer(text):
                target = local_target(source, match.group(1))
                if target is not None:
                    self.assertTrue(target.is_file(), f"{source}: {match.group(1)}")

    def test_html_entry_points_are_accessible_and_local(self):
        for source in (DOCS / "index.html", DOCS / "guide.html"):
            parser = PageParser()
            parser.feed(source.read_text(encoding="utf-8"))
            self.assertTrue(parser.lang, source)
            self.assertEqual(parser.main, 1, source)
            self.assertEqual(parser.h1, 1, source)
            for target in parser.links + parser.scripts + parser.styles:
                resolved = local_target(source, target)
                if resolved is not None:
                    self.assertTrue(resolved.is_file(), f"{source}: {target}")

    def test_dashboard_has_labeled_file_input(self):
        parser = PageParser()
        parser.feed((DOCS / "index.html").read_text(encoding="utf-8"))
        self.assertGreaterEqual(parser.labels, 1)

    def test_architecture_diagram_has_equivalent_prose(self):
        text = (DOCS / "architecture.md").read_text(encoding="utf-8")
        self.assertIn("```mermaid", text)
        self.assertIn("**Equivalent prose:**", text)

    def test_planning_status_and_schema_are_aligned(self):
        release = (ROOT / "release.md").read_text(encoding="utf-8")
        self.assertIn("BLOCKED_PUBLICATION_NOT_AUTHORIZED", release)
        for path in (ROOT / "README.md", ROOT / "taskchain.md", ROOT / "punchlist.md", ROOT / "release.md", ROOT / "changelog.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn("publication", text.lower(), path)
        for path in (ROOT / "README.md", ROOT / "taskchain.md", ROOT / "release.md", DOCS / "report-schema.md"):
            self.assertIn("1.0", path.read_text(encoding="utf-8"), path)

    def test_publication_authority_remains_absent(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        triggers, uses, permissions = workflow_structure(workflow)
        self.assertNotRegex(triggers, r"(?m)^\s*push\s*:")
        self.assertNotRegex(triggers, r"(?m)^\s*workflow_dispatch\s*:")
        self.assertEqual(permissions, ["contents: read"])
        prohibited_actions = ("actions/deploy-pages@", "actions/configure-pages@", "actions/upload-pages-artifact@")
        for action in uses:
            self.assertFalse(action.startswith(prohibited_actions), action)

    def test_skill_mapping_and_gap_are_recorded(self):
        text = (ROOT / "taskchain.md").read_text(encoding="utf-8")
        for category in ("CAT-011", "CAT-012", "CAT-017", "CAT-019", "CAT-031", "CAT-052", "CAT-054", "CAT-056", "CAT-064"):
            self.assertIn(category, text)
        self.assertIn("056-F", text)
        self.assertIn("non-authoritative", text)


if __name__ == "__main__":
    unittest.main()
