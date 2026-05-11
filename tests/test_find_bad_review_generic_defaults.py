import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = REPO_ROOT / "skills" / "find-bad-review" / "SKILL.md"
SOURCE_ADAPTERS_PATH = (
    REPO_ROOT / "skills" / "find-bad-review" / "references" / "source-adapters.md"
)
REPORT_TEMPLATE_PATH = (
    REPO_ROOT / "skills" / "find-bad-review" / "assets" / "report-template.md"
)
SCRIPT_PATH = (
    REPO_ROOT / "skills" / "find-bad-review" / "scripts" / "render_report_stub.py"
)


def load_render_report_stub():
    spec = importlib.util.spec_from_file_location("render_report_stub", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class FindBadReviewGenericDefaultsTest(unittest.TestCase):
    def test_report_template_does_not_bake_in_chewy(self):
        template = REPORT_TEMPLATE_PATH.read_text()

        self.assertNotIn("Chewy", template)

    def test_skill_workflow_does_not_name_pet_retailers_as_default_channels(self):
        skill = SKILL_PATH.read_text()

        self.assertNotIn("Chewy", skill)
        self.assertNotIn("pet care", skill)

    def test_source_adapters_do_not_treat_chewy_as_a_first_class_generic_channel(self):
        source_adapters = SOURCE_ADAPTERS_PATH.read_text()

        self.assertNotIn("## Chewy", source_adapters)
        self.assertNotIn("pet products", source_adapters)

    def test_render_report_stub_default_channels_are_generic(self):
        module = load_render_report_stub()
        report = module.build_report("Sample product", ["amazon", "retailer", "forum"])

        self.assertIn("| amazon |", report)
        self.assertIn("| retailer |", report)
        self.assertIn("| forum |", report)
        self.assertNotIn("| chewy |", report)


if __name__ == "__main__":
    unittest.main()
