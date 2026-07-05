import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
VERIFY_ROOT = REPO_ROOT / "skills" / "verify-idea"
SKILL_PATH = VERIFY_ROOT / "SKILL.md"
LENSES_PATH = VERIFY_ROOT / "references" / "validation-lenses.md"
REPORT_FORMAT_PATH = VERIFY_ROOT / "references" / "report-format.md"
REPORT_TEMPLATE_PATH = VERIFY_ROOT / "assets" / "report-template.md"
SCRIPT_PATH = VERIFY_ROOT / "scripts" / "render_report_stub.py"
EVIDENCE_STANDARD_PATH = REPO_ROOT / "references" / "evidence-standard.md"
OPENAI_AGENT_PATH = VERIFY_ROOT / "agents" / "openai.yaml"
README_PATH = REPO_ROOT / "README.md"

REQUIRED_DIMENSIONS = [
    "Market existence / why this market exists",
    "Buyer motivation / stable need",
    "Differentiation",
    "CAC proxy / acquisition pressure",
    "LTV / repeat or retention logic",
    "Content and SEO fit",
    "Photo, video, UGC, and review fit",
    "AI readability / citation / support fit",
    "Logistics and fulfillment risk",
    "Compliance and platform-policy risk",
    "Margin / unit-economics plausibility",
    "After-sales and support complexity",
    "Brand compounding potential",
]


def load_render_report_stub():
    spec = importlib.util.spec_from_file_location("verify_idea_stub", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class VerifyIdeaCommercialViabilityTest(unittest.TestCase):
    def test_skill_requires_baseline_viability_dimensions(self):
        skill = SKILL_PATH.read_text()

        self.assertIn("Every report must include", skill)
        self.assertIn("mark it `unclear`", skill)
        for phrase in [
            "market existence",
            "buyer motivation",
            "acquisition economics",
            "LTV",
            "content and discoverability",
            "after-sales",
            "brand compounding",
        ]:
            self.assertIn(phrase, skill)

    def test_lenses_define_commercial_viability_topics(self):
        lenses = LENSES_PATH.read_text()

        for heading in [
            "Market Existence And Need Stability",
            "Buyer Motivation",
            "Differentiation",
            "Acquisition Economics And CAC Proxy",
            "LTV Or Repeat-Purchase Plausibility",
            "Content And Discoverability Fit",
            "Margin And Unit-Economics Plausibility",
            "After-Sales Drag",
            "Brand Compounding Potential",
        ]:
            self.assertIn(heading, lenses)

    def test_report_surfaces_all_required_dimensions(self):
        for path in [REPORT_FORMAT_PATH, REPORT_TEMPLATE_PATH]:
            with self.subTest(path=path):
                text = path.read_text()
                self.assertIn("Commercial Viability Snapshot", text)
                for dimension in REQUIRED_DIMENSIONS:
                    self.assertIn(dimension, text)

    def test_stub_outputs_all_required_dimensions(self):
        module = load_render_report_stub()
        report = module.build_report("Sample idea", ["demand", "brand"])

        self.assertIn("## Commercial Viability Snapshot", report)
        for dimension in REQUIRED_DIMENSIONS:
            self.assertIn(dimension, report)

    def test_research_requires_source_vetting_and_numeric_confidence(self):
        evidence_standard = EVIDENCE_STANDARD_PATH.read_text()
        research_rules = (VERIFY_ROOT / "references" / "research-rules.md").read_text()
        report_format = REPORT_FORMAT_PATH.read_text()
        template = REPORT_TEMPLATE_PATH.read_text()

        self.assertIn("Source Vetting", evidence_standard)
        self.assertIn("X rant", evidence_standard)
        self.assertIn("Corroboration Standard", evidence_standard)
        self.assertIn("Do not score above `6/10`", research_rules)
        self.assertIn("Confidence / 10", report_format)
        self.assertIn("Corroboration status", template)

    def test_entrypoint_and_skill_body_make_report_contract_mandatory(self):
        agent = OPENAI_AGENT_PATH.read_text()
        skill = SKILL_PATH.read_text()

        self.assertIn("must include the full report contract", agent)
        self.assertIn("Commercial Viability Snapshot", agent)
        self.assertIn("full report on the final recommended SKU", agent)
        self.assertIn("The final answer is incomplete unless", skill)
        self.assertIn("A hero-SKU recommendation without the complete report", skill)
        self.assertNotIn("should usually include", skill)

    def test_product_finding_requests_are_multi_skill_pipeline(self):
        agent = OPENAI_AGENT_PATH.read_text()
        skill = SKILL_PATH.read_text()
        readme = README_PATH.read_text()

        for text in [agent, skill, readme]:
            self.assertIn("find-bad-review", text)
            self.assertIn("analyze-competitor", text)
            self.assertIn("portray-audience", text)
        self.assertIn("Product Opportunity Workflow", readme)
        self.assertIn("multi-skill product-opportunity pipeline", skill)


if __name__ == "__main__":
    unittest.main()
