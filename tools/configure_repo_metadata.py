#!/usr/bin/env python3
"""Configure GitHub About descriptions and topics (dry-run unless --apply).

Requires the human owner's own authenticated GitHub CLI:
    gh auth login
    python tools/configure_repo_metadata.py
    python tools/configure_repo_metadata.py --apply

No access tokens or passwords are embedded or requested by this script.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

OWNER = "Morteza-fatemi"
METADATA = {
    "darik-ai-overview": (
        "Public architecture and evidence-based agentic AI case study; no proprietary backend.",
        ["agentic-ai", "llm", "privacy", "system-design", "case-study", "persian"]),
    "shopbani-platform": (
        "Sanitized full-stack e-commerce operations case study with a fictional offline demo.",
        ["ecommerce", "nextjs", "nestjs", "postgresql", "redis", "case-study"]),
    "sepand-platform": (
        "Privacy-aware school transport architecture case study and fictional workflow demo.",
        ["system-design", "transportation", "rbac", "data-integrity", "case-study"]),
    "roniq-ai-platform": (
        "Public design notes for Persian RTL conversational interfaces and reversible knowledge edits.",
        ["conversational-ai", "rtl", "ui-ux", "case-study", "architecture"]),
    "vahedha-platform": (
        "Laravel and Jalali data-workflow architecture notes; application source remains private.",
        ["laravel", "jalali", "persian", "architecture", "case-study"]),
    "ai-browser-agent": (
        "Public reference architecture for bounded browser agents, consent and prompt-injection safety.",
        ["browser-agent", "ai-agent", "security", "architecture", "case-study"]),
    "notbox": (
        "Python and Windows notebook-app engineering notes about local data safety.",
        ["python", "windows", "notebook", "architecture", "case-study"]),
    "ivsi-platform": (
        "Public IVSI systems-engineering design notes; no unverified production claims.",
        ["system-design", "backend", "architecture", "case-study"]),
    "wp-pro-votes": (
        "WordPress voting-plugin design considerations, eligibility and replay prevention.",
        ["wordpress", "voting", "php", "security", "case-study"]),
    "chatline-platform": (
        "Communication workflow architecture: messaging privacy, ordering and retries.",
        ["messaging", "realtime", "system-design", "case-study"]),
    "bobo-audio": (
        "Windows offline voice assistant with Win32 hotkeys and opt-in secured local remote.",
        ["python", "windows", "vosk", "voice-assistant", "win32", "offline"]),
    "rapfa-music-search": (
        "Persian music search with Node.js, safe static serving and Chromium E2E tests.",
        ["nodejs", "javascript", "music-search", "playwright", "rtl"]),
    "Morteza-fatemi": (
        "Engineering portfolio: backend systems, AI architecture and verified project case studies.",
        ["portfolio", "full-stack", "backend", "applied-ai"]),
}


def api(path: str, method: str = "GET", data: dict | None = None) -> dict:
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json",
           "--method", method, path]
    if data is not None:
        cmd += ["--input", "-"]
    result = subprocess.run(cmd, text=True, input=json.dumps(data) if data is not None else None,
                            capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"API failed: {method} {path}")
    return json.loads(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Actually update descriptions/topics for these public repos")
    opts = parser.parse_args()
    if not opts.apply:
        print("DRY RUN: no network requests or edits. Planned metadata:")
        for name, (description, topics) in METADATA.items():
            print(f"- {OWNER}/{name}\n  Description: {description}\n  Topics: {', '.join(topics)}")
        print("\nRun with --apply only after signing in through gh auth login.")
        return 0
    if not shutil.which("gh"):
        print("Install GitHub CLI from https://cli.github.com/", file=sys.stderr)
        return 1
    try:
        user = api("user")
        if user.get("login", "").casefold() != OWNER.casefold():
            print(f"Refusing to run: gh is signed in as {user.get('login')}, not {OWNER}",file=sys.stderr)
            return 1
    except Exception as e:
        print(f"Cannot validate GitHub CLI login: {e}",file=sys.stderr)
        return 1

    failures = 0
    for repo, (description, desired) in METADATA.items():
        try:
            path = f"repos/{OWNER}/{repo}"
            current = api(path)
            if not current.get("permissions", {}).get("admin"):
                raise PermissionError(f"Administrative permission not available for {repo}")
            if current.get("description") != description:
                api(path, "PATCH", {"description": description})
            current_topics = api(path + "/topics").get("names", [])
            union = sorted(set(current_topics) | set(desired))
            if len(union) > 20:
                raise ValueError("More than 20 topics; review manually to avoid dropping existing topics")
            if set(current_topics) != set(union):
                api(path + "/topics", "PUT", {"names": union})
            verify = api(path)
            result_topics = api(path + "/topics").get("names", [])
            if verify.get("description") != description or not set(desired).issubset(result_topics):
                raise RuntimeError("Updated metadata could not be verified")
            print(f"PASS: {repo}: description and {len(result_topics)} topics verified")
        except Exception as e:
            failures += 1
            print(f"FAILED: {repo}: {e}",file=sys.stderr)
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
