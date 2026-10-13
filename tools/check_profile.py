"""Validate that portfolio links are not repeated within a rendered line."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT / "README.md").read_text(encoding="utf-8")
errors = []
for number, line in enumerate(readme.splitlines(), 1):
    # Only compare Markdown target URLs on a line; one project can be mentioned
    # in multiple sections without incorrectly flagging a duplicate.
    links = re.findall(r"\]\((https?://[^)]+)\)", line)
    if len(links) != len(set(links)):
        errors.append(f"README.md:{number}: duplicate target URL in one line")
for target in ("darik-ai-overview/blob/main/demo/index.html",
               "bobo-audio/releases/tag/v0.1.0",
               "rapfa-music-search/releases/tag/v0.1.0",
               "shopbani-platform/blob/main/CASE_STUDY.md",
               "sepand-platform/blob/main/CASE_STUDY.md"):
    if target not in readme:
        errors.append("Required portfolio link missing: " + target)
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("PASS: profile has no repeated URLs per line and key project links exist")
