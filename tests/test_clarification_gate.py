from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills"
SKILL_NAMES = [
    "find-bad-review",
    "analyze-competitor",
    "portray-audience",
    "verify-idea",
]


class ClarificationGateTest(unittest.TestCase):
    def test_each_skill_defines_a_flexible_clarification_gate(self):
        for skill_name in SKILL_NAMES:
            with self.subTest(skill=skill_name):
                skill = (SKILL_ROOT / skill_name / "SKILL.md").read_text()

                self.assertIn("## Clarification Gate", skill)
                self.assertIn("one clarification question at a time", skill)
                self.assertIn("2-3 concrete options", skill)
                self.assertIn("Do not ask a fixed number of questions", skill)
                self.assertIn("materially affects evidence collection", skill)

    def test_readme_documents_package_clarification_policy(self):
        readme = (REPO_ROOT / "README.md").read_text()

        self.assertIn("Clarification Policy", readme)
        self.assertIn("small options", readme)
        self.assertIn("not a full planning mode", readme)


if __name__ == "__main__":
    unittest.main()
