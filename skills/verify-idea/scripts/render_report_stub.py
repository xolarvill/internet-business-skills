#!/usr/bin/env python3

import argparse


def build_report(idea: str, lenses: list[str]) -> str:
    lens_text = ", ".join(lenses)
    return f"""# Idea Verification Report

## Idea Statement

- Idea: {idea}
- Geography:
- Channel:
- Target customer:
- Matching note:

## Claim Ledger

| Claim | Verdict | Confidence | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Commercial Viability Snapshot

| Dimension | Readout | Confidence | Evidence or gap |
| --- | --- | --- | --- |
| Market existence / why this market exists |  |  |  |
| Buyer motivation / stable need |  |  |  |
| Differentiation |  |  |  |
| CAC proxy / acquisition pressure |  |  |  |
| LTV / repeat or retention logic |  |  |  |
| Content and SEO fit |  |  |  |
| Photo, video, UGC, and review fit |  |  |  |
| AI readability / citation / support fit |  |  |  |
| Logistics and fulfillment risk |  |  |  |
| Compliance and platform-policy risk |  |  |  |
| Margin / unit-economics plausibility |  |  |  |
| After-sales and support complexity |  |  |  |
| Brand compounding potential |  |  |  |

## Coverage Summary

| Source type | What it informed | Evidence quality | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Strongest Supporting Facts

- Fact:
  Supports:
  Why it matters:
  Sources:

## Strongest Weakening Facts

- Fact:
  Weakens:
  Why it matters:
  Sources:

## Verdict

- Verdict:
- What is supported:
- What is weakened:
- What remains unknown:

## Confidence And Gaps

- Lenses used: {lens_text}
- 

## Suggested Next Validation Step

- 
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a markdown starter report for fact-based idea verification."
    )
    parser.add_argument("--idea", required=True, help="Idea statement")
    parser.add_argument(
        "--lenses",
        nargs="+",
        default=[
            "demand",
            "buyer-motivation",
            "differentiation",
            "acquisition-economics",
            "content-fit",
            "operations",
            "brand",
        ],
        help="Validation lenses to foreground in the report",
    )
    args = parser.parse_args()
    print(build_report(args.idea, args.lenses))


if __name__ == "__main__":
    main()
