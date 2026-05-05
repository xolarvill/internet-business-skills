#!/usr/bin/env python3

import argparse


def build_report(target: str, lenses: list[str]) -> str:
    lens_text = ", ".join(lenses)
    return f"""# Audience Portrait Report

## Focal Target

- Focal target: {target}
- Category:
- Scope:
- Matching note:

## Coverage Summary

| Source type | Contribution | Evidence quality | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Intended Audience Signals

- 

## Observed Audience Clusters

### 1. Cluster

- Why this cluster exists:
- Motivation:
- Trust threshold:
- Price sensitivity:
- Confidence:

## Motivations And Objections

### 1. Cluster

- Motivation:
- Objection:
- What message or proof matters:

Example pages:
- 

## Weak-Fit Or Excluded Audiences

- 

## Commercial Judgments

- Judgment:
  Basis:
  Why it matters:

## Confidence And Gaps

- Lenses used: {lens_text}
- 

## Suggested Next Move

- 
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a markdown starter report for public audience portrayal."
    )
    parser.add_argument("--target", required=True, help="Target product or brand name")
    parser.add_argument(
        "--lenses",
        nargs="+",
        default=["positioning", "motivations", "objections", "fit-signals"],
        help="Audience lenses to foreground in the report",
    )
    args = parser.parse_args()
    print(build_report(args.target, args.lenses))


if __name__ == "__main__":
    main()
