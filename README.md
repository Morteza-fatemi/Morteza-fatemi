<div align="center">

# Seyyed Morteza Fatemi Zade
**Full-Stack Software Engineer · Backend Architecture · Applied AI**

Designing web platforms, operational backends, and evidence-aware AI integrations.

[Case studies](#selected-projects) · [Open source & checks](#public-code--automated-quality) · [Technical focus](#technical-focus) · [Contact](#contact)

</div>

## Selected projects

### [Darik AI — Agentic business-assistant architecture](https://github.com/Morteza-fatemi/darik-ai-overview)
An engineering-oriented public overview of a Persian-first, privacy-conscious AI gateway with scoped tools, verifiable numeric answers, policy boundaries and bounded agent plans.

[Architecture](https://github.com/Morteza-fatemi/darik-ai-overview/blob/main/ARCHITECTURE.md) · [Security / threat model](https://github.com/Morteza-fatemi/darik-ai-overview/blob/main/SECURITY_MODEL.md) · [Engineering decisions](https://github.com/Morteza-fatemi/darik-ai-overview/blob/main/ENGINEERING_DECISIONS.md) · [Offline synthetic demo](https://github.com/Morteza-fatemi/darik-ai-overview/blob/main/demo/index.html)

`TypeScript` `NestJS` `AI/LLM` `Data access policy` `Evaluation`

*The repository documents design boundaries; it does not publish the private application source or attest to production maturity.*

### [ShopBani — E-commerce platform operations](https://github.com/Morteza-fatemi/shopbani-platform)
Multi-surface commerce engineering: Next.js customer/admin experiences, NestJS services, persistence, background processing, asset storage, reliability and incident diagnosis.

[Operational case study](https://github.com/Morteza-fatemi/shopbani-platform/blob/main/CASE_STUDY.md) · [Architecture](https://github.com/Morteza-fatemi/shopbani-platform/blob/main/ARCHITECTURE.md) · [Offline synthetic dashboard](https://github.com/Morteza-fatemi/shopbani-platform/blob/main/demo/index.html)

`Next.js` `NestJS` `PostgreSQL` `MongoDB` `Redis` `Linux`

*The interactive demo is entirely fictional and does not connect to an operational store.*

### [Sepand — Multi-role school transportation workflows](https://github.com/Morteza-fatemi/sepand-platform)
Technical case study on guardian, school and driver roles; scoped permissions, absence/attendance records, stale location data, payment transitions and reference-data reconciliation.

[Case study](https://github.com/Morteza-fatemi/sepand-platform/blob/main/CASE_STUDY.md) · [Access and state architecture](https://github.com/Morteza-fatemi/sepand-platform/blob/main/ARCHITECTURE.md) · [Offline synthetic workflow](https://github.com/Morteza-fatemi/sepand-platform/blob/main/demo/index.html)

`Backend` `RBAC` `Realtime data` `State integrity` `Privacy`

*No student, driver, vehicle, route or GPS data from the real system is published.*

## Public code & automated quality

| Repository | What you can inspect | CI |
| --- | --- | --- |
| [BOBO — offline Windows voice assistant](https://github.com/Morteza-fatemi/bobo-audio) | Real Python application; Windows API hooks; secure opt-in web remote; regression tests | [Quality](https://github.com/Morteza-fatemi/bobo-audio/actions/workflows/quality.yml) · [v0.1.0 source release](https://github.com/Morteza-fatemi/bobo-audio/releases/tag/v0.1.0) |
| [Rapfa — public music search](https://github.com/Morteza-fatemi/rapfa-music-search) | Node.js API, safe static server, build, official embed integration and browser tests | [Quality](https://github.com/Morteza-fatemi/rapfa-music-search/actions/workflows/quality.yml) · [v0.1.0 source release](https://github.com/Morteza-fatemi/rapfa-music-search/releases/tag/v0.1.0) · [v0.1.0 source release](https://github.com/Morteza-fatemi/rapfa-music-search/releases/tag/v0.1.0) |

The public tests are evidence for their tested behaviors only. A hosted CI pass does not guarantee hardware compatibility or production security.

## Technical focus

- **Backend:** Node.js, NestJS, Express, Laravel, API design and asynchronous workflows.
- **Frontend:** Next.js, React, Persian RTL and responsive user interfaces.
- **Data:** PostgreSQL, MongoDB, Redis, data correctness and reliable state transitions.
- **Infrastructure:** Docker, Linux, application services, monitoring and CI/CD.
- **Applied AI:** Scoped tool calling, verifiable business calculations, retrieval, privacy boundaries and evaluation.

## Engineering principles

1. Treat user inputs and AI-generated actions as untrusted until validated by server-side policy.
2. Make claims traceable to reproducible tests, explicit data ranges and known limitations.
3. Design for partial failures, safe retries and measurable operations.
4. Keep commercial source code and users' sensitive information confidential.
5. Document trade-offs for the next engineer, not just the author.

## Contact

For engineering collaboration, open a GitHub discussion/issue in a suitable public project **without sensitive details**, or reach out through the GitHub profile.

*Public case studies and demos are engineering portfolio material; do not treat them as official statements by project customers or independently verified production benchmarks.*
