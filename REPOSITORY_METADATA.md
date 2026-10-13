# GitHub repository metadata — copy-ready settings

> This checklist documents suggested **GitHub About metadata**, which is **not stored in repository files**. It cannot be changed by editing a README. Requires a user/account with Repository Administration permissions: open the repository homepage → **About ⚙️**.

| Repository | Suggested short description | Suggested Topics (comma-separated) | Homepage suggestion |
| --- | --- | --- | --- |
| `darik-ai-overview` | Public architecture case study for a Persian-first, evidence-backed agentic AI gateway. | `ai-agent`, `llm`, `nestjs`, `architecture`, `privacy`, `case-study` | Repository README (omit homepage if none) |
| `shopbani-platform` | Sanitized full-stack e-commerce operations case study with an offline synthetic demo. | `ecommerce`, `nextjs`, `nestjs`, `postgresql`, `redis`, `case-study` | Approved official product URL only |
| `sepand-platform` | School transport engineering case study covering RBAC, attendance and data integrity. | `transportation`, `rbac`, `system-design`, `realtime`, `case-study` | No public private-system URL |
| `bobo-audio` | Offline Windows voice assistant with optional secured local web remote and Win32 regression checks. | `python`, `windows`, `voice-assistant`, `vosk`, `win32`, `offline` | Repository README until a public demo exists |
| `rapfa-music-search` | Persian music search frontend and Node.js API with Chromium E2E and safe static serving. | `nodejs`, `javascript`, `persian`, `music-search`, `playwright`, `rtl` | Public UI URL only if user verifies deployment |

## Ready-to-open repository URLs
- https://github.com/Morteza-fatemi/darik-ai-overview
- https://github.com/Morteza-fatemi/shopbani-platform
- https://github.com/Morteza-fatemi/sepand-platform
- https://github.com/Morteza-fatemi/bobo-audio
- https://github.com/Morteza-fatemi/rapfa-music-search

## Safe public demos
- ShopBani (fake operational data): https://github.com/Morteza-fatemi/shopbani-platform/blob/main/demo/index.html
- Sepand (fake child and route identifiers): https://github.com/Morteza-fatemi/sepand-platform/blob/main/demo/index.html
- Darik (fake deterministic AI analytics): https://github.com/Morteza-fatemi/darik-ai-overview/blob/main/demo/index.html

These are **source HTML files**, not deployed GitHub Pages sites. Download and open locally. Do not claim a working live production demo.

## Pin repositories to the profile
Open profile → **Customize your pins**. Recommended six pins:
`darik-ai-overview`, `shopbani-platform`, `sepand-platform`, `bobo-audio`, `rapfa-music-search`, and one independently verifiable public-code project.

## Release and integrity rules
- Do not list a new public tag as a production release of a proprietary customer system.
- Do not upload any secrets, GPS traces, order exports, real student records or environment files to public repositories.
- Metadata/Homepage fields and pins require GitHub UI/API administration permission; saving this checklist does **not** change the actual About settings.
