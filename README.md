# AI Agent Card

**Making agentic AI transparent, auditable and controllable — one card at a time.**

A standardized, machine-readable and human-readable card for documenting agentic AI systems.  
Designed for transparency, human agency, regulatory compliance (EU AI Act), security (OWASP Agentic Top 10), and governance frameworks (ISO 27001:2022 + ISO/IEC 42001).

## Why AI Agent Card?

As agentic AI systems become more autonomous, opacity becomes a major risk.  
This standard provides a practical, governance-first "passport" for every deployed agent — making its goal, capabilities, autonomy level, human oversight mechanisms, risk mitigations, and treatment plan explicit and verifiable.

It complements discovery-focused Agent Cards (e.g., A2A protocol) by adding deep governance, risk treatment, and accountability layers.

## Features
- Full support for **EU AI Act** risk classifications and obligations
- Detailed **OWASP Top 10 for Agentic Applications** mitigations (per-risk)
- Structured **risk treatment plan** with direct mapping to ISO 27001:2022 and ISO/IEC 42001 Clause 8 (Operation)
- Explicit **human oversight** ("how" it works, not just that it exists)
- **EBSI Verifiable Credential** ready (decentralized, cryptographically verifiable)
- Lightweight validation script + examples
- Designed for both individual researchers and enterprise ISMS/AIMS

## Current Version
**Draft v0.3** (RFC stage) — Actively seeking feedback and real-world use cases.

## Quick Start
1. Clone or download the schema: [`agent-card-v0.3.json`](./agent-card-v0.3.json)
2. Fill your agent card (start from the [Grok Research Assistant example](./examples/grok-research-assistant.json))
3. Validate: `python validate-agent-card.py your-agent-card.json`
4. Publish as JSON or wrap as an EBSI Verifiable Credential

## Repository Contents
- `agent-card-v0.3.json` — Full JSON Schema
- `validate-agent-card.py` — Lightweight validation script
- `examples/` — Populated examples (including Grok-based)
- `docs/` — Additional guidance (coming in future releases)

## Documentation
- [Schema Documentation](./docs/schema.md) (add later)
- [Risk Treatment Plan Guide](./docs/risk-treatment-plan.md) (add later)

## Contributing
We welcome contributions from AI governance, cybersecurity, standards, and policy professionals.  
See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## License
MIT License — see [LICENSE](./LICENSE)

## Related Work
- [Worldview Belief System Card (WBSC)](https://github.com/rumagoso/worldview-belief-system-card) — Companion standard for base model/worldview transparency
- EU AI Act, OWASP Agentic AI Top 10, ISO/IEC 42001, ISO 27001:2022

---

**Maintained by Rui Soares** — Focused on practical transparency and human agency in AI.

Feedback, issues, and pull requests are welcome!
