# Enable main branch protection — 13 repositories

**Status:** Prepared; **not automatically applied** by the GitHub connector. The connected GitHub App can modify repository files and pull requests but does not expose repository administration/ruleset mutations, even if the account itself is an administrator.

## Preferred: one-time GitHub CLI setup (Windows, Mac, Linux)

1. Install the official [GitHub CLI](https://cli.github.com/).
2. Open PowerShell or a terminal, run `gh auth login`, and authenticate in your **own browser**. Never paste authentication tokens into this repository, an Issue, or a chat.
3. Download or clone this profile repository; from its root run:
   ```powershell
   python tools/protect_main.py
   python tools/protect_main.py --apply
   ```
4. The script checks whether main is already protected before making changes, then verifies protection and required CI after applying. Existing protections are **never overwritten automatically**. If a repository is already protected, compare its rule manually.

## Policy being applied

- Target: `main`.
- Require successful checks (and up-to-date branch) **before merging**.
- Require a pull request, with **zero mandatory approvals** to avoid blocking a solo maintainer.
- Enforce rules on administrators; require resolution of review conversations.
- Deny force-push and branch deletion.
- Preserve repository-specific push permissions and original source code.

| Repository | Required status checks |
| --- | --- |
| [BOBO](https://github.com/Morteza-fatemi/bobo-audio/settings/branches) | `python-hygiene`, `windows-native-smoke` |
| [Rapfa](https://github.com/Morteza-fatemi/rapfa-music-search/settings/branches) | `verify`, `browser-e2e` |
| [Darik](https://github.com/Morteza-fatemi/darik-ai-overview/settings/branches) | `docs-validation` |
| [ShopBani](https://github.com/Morteza-fatemi/shopbani-platform/settings/branches) | `public-case-study` |
| [Sepand](https://github.com/Morteza-fatemi/sepand-platform/settings/branches) | `public-case-study` |
| Roniq, Vahedha, AI Browser Agent, Notbox, IVSI, WP Pro Votes, Chatline | `public-docs` (each repository) |
| Profile README | `profile-quality` |

## Configure repository About descriptions and topics

An optional companion script, `tools/configure_repo_metadata.py`, prepares accurate public descriptions and topics for all 13 repositories, requires GitHub CLI authentication, preserves existing topics and verifies updates. Run `python tools/configure_repo_metadata.py` for dry-run and add `--apply` only when ready.

Do not assign an invented public Homepage to demos that have not been deployed. Repository pins are configured separately in GitHub's profile UI.

## Manual fallback (GitHub UI)

For each repository open **Settings → Branches → Add branch protection rule** (or **Settings → Rules → Rulesets**, depending on the UI and plan). Select `main`, enable required Pull Request and required status checks, and enter the exact context names from the table. Require up-to-date branches, reject force pushes and deletion, and apply protection to administrators. Avoid requiring one approving reviewer for a solo-maintained repo unless a reviewer is available.

A CI YAML file by itself **does not block bad commits**. GitHub must confirm a `protected: true` branch or an active matching ruleset. To verify with your own account: `gh api repos/Morteza-fatemi/bobo-audio/branches/main --jq .protected` (repeat for other repositories). For branch-protection details: `gh api repos/Morteza-fatemi/bobo-audio/branches/main/protection`.

**Limitations:** This setup is explicit and may change branch management behavior; check any automation that pushes directly to main. If your repository has an existing ruleset or policy, review it before enabling another one. Branch settings are not stored in source code and cannot be activated merely by merging this document.
