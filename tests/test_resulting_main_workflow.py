from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
WORKFLOWS = ROOT / ".github/workflows"
RESULTING = WORKFLOWS / "resulting-main-validation.yml"


class ResultingMainWorkflowTests(unittest.TestCase):
    def test_each_validation_result_is_checked(self):
        text = RESULTING.read_text(encoding="utf-8")
        for step_id in ("collector", "javascript", "dashboard", "tests", "integrity"):
            self.assertIn(f"id: {step_id}", text)
            self.assertIn(f"steps.{step_id}.outputs.status", text)
        for status in (
            "COLLECTOR_STATUS",
            "JAVASCRIPT_STATUS",
            "DASHBOARD_STATUS",
            "TEST_STATUS",
            "INTEGRITY_STATUS",
        ):
            self.assertIn(f'test "${status}" = "0"', text)

    def test_push_generations_do_not_cancel_each_other(self):
        text = RESULTING.read_text(encoding="utf-8")
        self.assertIn("github.event_name == 'push' && github.sha", text)

    def test_failure_evidence_is_always_uploaded(self):
        text = RESULTING.read_text(encoding="utf-8")
        upload = text.split("- name: Upload retained exact-head evidence", 1)[1].split(
            "- name: Fail closed", 1
        )[0]
        self.assertIn("if: always()", upload)

    def test_all_workflow_changes_trigger_validation(self):
        text = RESULTING.read_text(encoding="utf-8")
        self.assertGreaterEqual(text.count('".github/workflows/**"'), 2)

    def test_all_workflows_are_scanned_for_deploy_authority(self):
        text = RESULTING.read_text(encoding="utf-8")
        self.assertIn("glob('*.yml')", text)
        self.assertIn("glob('*.yaml')", text)
        self.assertIn("prohibited_permission_patterns", text)
        self.assertIn("prohibited_action_prefixes", text)

    def test_remote_dashboard_assets_fail_closed(self):
        text = RESULTING.read_text(encoding="utf-8")
        self.assertIn("remote asset prohibited", text)
        self.assertIn("not parsed.scheme", text)
        self.assertIn("not parsed.netloc", text)

    def test_workflow_remains_read_only(self):
        text = RESULTING.read_text(encoding="utf-8")
        permissions = text.split("permissions:", 1)[1].split("concurrency:", 1)[0]
        lines = [line.strip() for line in permissions.splitlines() if ":" in line]
        self.assertEqual(lines, ["contents: read"])
        self.assertNotRegex(text, re.compile(r"(?m)^\s*pages\s*:\s*write\s*$"))
        self.assertNotRegex(text, re.compile(r"(?m)^\s*id-token\s*:\s*write\s*$"))


if __name__ == "__main__":
    unittest.main()
