#!/usr/bin/env python3
"""Apply main branch protection across the 13 public repositories using GitHub CLI.

Run: gh auth login && python tools/protect_main.py --apply
Without --apply: read-only plan. Never requests or embeds personal tokens.
Requires GitHub CLI authenticated as a repository administrator.
"""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys

OWNER = "Morteza-fatemi"
CHECKS = {
    "bobo-audio": ["python-hygiene", "windows-native-smoke"],
    "rapfa-music-search": ["verify", "browser-e2e"],
    "darik-ai-overview": ["docs-validation"],
    "shopbani-platform": ["public-case-study"],
    "sepand-platform": ["public-case-study"],
    "roniq-ai-platform": ["public-docs"],
    "vahedha-platform": ["public-docs"],
    "ai-browser-agent": ["public-docs"],
    "notbox": ["public-docs"],
    "ivsi-platform": ["public-docs"],
    "wp-pro-votes": ["public-docs"],
    "chatline-platform": ["public-docs"],
    "Morteza-fatemi": ["profile-quality"],
}

def gh_json(endpoint: str, method: str = "GET", payload: dict | None = None) -> dict:
    args = ["gh", "api", "-H", "Accept: application/vnd.github+json",
            "--method", method, endpoint]
    if payload is not None:
        args.extend(["--input", "-"])
    run = subprocess.run(args, input=json.dumps(payload) if payload is not None else None,
                         capture_output=True, text=True, check=False)
    if run.returncode:
        raise RuntimeError(f"GitHub CLI {method} {endpoint}: {run.stderr.strip()}")
    return json.loads(run.stdout)

def protection(checks: list[str]) -> dict:
    return {
        "required_status_checks": {"strict": True, "contexts": checks},
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 0,
        },
        "restrictions": None,
        "required_conversation_resolution": True,
        "allow_force_pushes": False,
        "allow_deletions": False,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Actually enable protections using gh auth")
    options = parser.parse_args()
    print("Repositories and required checks:")
    for name, checks in CHECKS.items():
        print(f"  {OWNER}/{name}: {', '.join(checks)}")
    if not options.apply:
        print("\nDry run only: no changes made. Use --apply to execute.")
        return 0
    if not shutil.which("gh"):
        print("GitHub CLI missing: install https://cli.github.com/ then gh auth login", file=sys.stderr)
        return 1
    failures = 0
    for name, checks in CHECKS.items():
        endpoint = f"repos/{OWNER}/{name}/branches/main"
        try:
            branch = gh_json(endpoint)
            if branch.get("protected"):
                print(f"SKIP {name}: already protected; inspect existing settings manually to avoid overwriting them")
                continue
            gh_json(endpoint + "/protection", method="PUT", payload=protection(checks))
            verified = gh_json(endpoint)
            policy = gh_json(endpoint + "/protection")
            contexts = set((policy.get("required_status_checks") or {}).get("contexts") or [])
            if not verified.get("protected") or not set(checks).issubset(contexts):
                raise RuntimeError("Protection or required checks not confirmed after applying")
            print(f"OK {name}: main protected; required checks: {', '.join(checks)}")
        except Exception as exc:
            failures += 1
            print(f"FAILED {name}: {exc}", file=sys.stderr)
    if failures:
        print(f"FAILED: {failures} repo(s) need attention; see BRANCH_PROTECTION.md", file=sys.stderr)
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
