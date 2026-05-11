#!/usr/bin/env python3

import argparse


def build_report(product: str, channels: list[str]) -> str:
    rows = "\n".join(
        f"| {channel} |  |  |  |" for channel in channels
    )
    return f"""# Representative Bad Review Report

## Product Target

- Product: {product}
- Brand:
- Variant:
- Matching note:

## Coverage Summary

| Channel | Source count | Evidence quality | Notes |
| --- | --- | --- | --- |
{rows}

## Top Complaint Themes

### 1. Theme

- Why it matters:
- Confidence:
- Spread:

Representative evidence:

- 

### 2. Theme

- Why it matters:
- Confidence:
- Spread:

Representative evidence:

- 

## Cross-Channel Patterns

- 

## Confidence And Gaps

- 

## Suggested Next Step

- 
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a markdown starter report for representative bad review research."
    )
    parser.add_argument("--product", required=True, help="Product name")
    parser.add_argument(
        "--channels",
        nargs="+",
        default=["amazon", "walmart", "reddit", "tiktok", "retailer", "forum"],
        help="Channels to include in the coverage summary",
    )
    args = parser.parse_args()
    print(build_report(args.product, args.channels))


if __name__ == "__main__":
    main()
