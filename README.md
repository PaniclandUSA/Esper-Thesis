# ESPER-THESIS

**Semantic Research Management & Academic Organization System**

Part of the ESPER-STACK ecosystem supporting literacy liberation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://github.com/PaniclandUSA/Esper-Thesis)

---

## 🎯 Mission

ESPER-THESIS advances **The Cyrano de Bergerac Foundation**'s mission to help **4 million Americans achieve literacy by 2030** by providing a transparent, auditable, zero-dependency research intelligence system.

This tool transforms raw research, insights, field notes, and AI validations into structured, analyzable semantic packets.

> *"Teaching a neighbor to read is a labor of love."*

---

## ✨ What is ESPER-THESIS?

A semantic intelligence system that performs **multi-agent academic analysis**, turning research chaos into clarity using a 5-agent pipeline:

1. **Theoretical Agent** – Coherence, logic, breakthrough potential
2. **Empirical Agent** – Evidence quality, reproducibility
3. **Novelty Agent** – Originality, lineage, paradigm shifts
4. **Impact Agent** – Mission alignment, societal/industry significance
5. **Synthesis Agent** – Cross-packet connections and semantic overlap

Each research finding becomes a **ResearchPacket** containing:

- **PICTOGRAM-256 semantic hash** (3-character glyph)
- **ChronoCore temporal marker**
- **VSE Protocol encoding** (intent, certainty, affect)
- **Deterministic routing decision** + priority score
- **Complete audit trail** (theoretical + empirical + novelty + impact + synthesis)

ESPER-THESIS is **zero dependencies**, fully portable, and safe to run in:

- NASA / SETI air-gapped environments
- University research labs
- Literacy nonprofits
- Field settings (Raspberry Pi, old laptops)
- Severe IT-restriction contexts

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/PaniclandUSA/Esper-Thesis.git
cd Esper-Thesis

# Install in development mode
pip install -e .
```

Or, once published:

```bash
pip install esper-thesis
```

### Create Your First Research Packet

```bash
esper-thesis create \
  --title "PICTOGRAM-256: Universal Semantic Communication" \
  --type theory \
  --abstract "A complete 256-glyph system with cryptographic binding" \
  --findings "8-bit isomorphism" "Geometric universals" "AI-validated"
```

Output:

```
✓ Created: a3f7b921
  Title: PICTOGRAM-256: Universal Semantic Communication
  Type: theory
  Routing: active_development
  Priority: 0.87
  Database: ./research_db.json
```

### List Research Packets

```bash
esper-thesis list --sort priority --limit 10
```

### Export Findings

```bash
# Markdown for documentation
esper-thesis export --format markdown --output findings.md

# JSON for databases/APIs
esper-thesis export --format json --output research.json

# Human-readable summaries
esper-thesis export --format summary
```

---

## 🗄️ Database Location

ESPER-THESIS supports **four-level priority resolution** to determine where research is stored.

### Resolution Order (Highest → Lowest)

**1. Explicit CLI argument** (highest priority)

```bash
esper-thesis --database ~/research/global.json create ...
```

**2. Environment variable**

```bash
export ESPER_THESIS_DB=~/research/main.json
esper-thesis create ...
```

**3. Config file** `~/.esper_thesis/config.json`

```json
{
  "default_database": "~/research/global.json",
  "projects": {
    "literacy": "~/projects/literacy/research.json",
    "nasa": "~/projects/nasa/db.json"
  }
}
```

Use with:

```bash
esper-thesis --project literacy create ...
```

**4. Default: Local file**

```
./research_db.json
```

### Why This Matters

✅ **Per-project research** – Keep findings isolated by context  
✅ **Global corpus** – Unified research database across all work  
✅ **Reproducible workflows** – Commit database with code in Git  
✅ **Zero breaking changes** – Default behavior unchanged from v1.0  

---

## 📚 Core Concepts

### ResearchPacket (Semantic Atomic Unit)

```python
from esper_thesis import process_research_item, ResearchType

packet = process_research_item(
    title="VSE Protocol Validation",
    abstract="Validated through 5-AI Turing Tour",
    key_findings=["95% reconstruction accuracy", "40% token compression"],
    research_type=ResearchType.VALIDATION,
    source="experiment"
)

print(packet.get_summary())
```

Each `ResearchPacket` contains:

- Multi-agent assessments (theoretical, empirical, novelty, impact, synthesis)
- PICTOGRAM-256 semantic hash
- ChronoCore temporal marker
- VSE Protocol encoding
- Routing decision + priority score
- Synthesis connections to related packets

### Research Types

| Type | Description |
|------|-------------|
| **THEORY** | Models, frameworks, conceptual structures |
| **VALIDATION** | Empirical tests, experiments, reproductions |
| **APPLICATION** | Real-world implementations |
| **INSIGHT** | Observations, field notes, conceptual sparks |
| **SYNTHESIS** | Integration across multiple packets |
| **QUESTION** | Open research inquiries |
| **BREAKTHROUGH** | Paradigm-shifting discoveries |

### Routing Logic

Packets are automatically routed based on multi-agent assessment:

| Routing | Criteria | Priority |
|---------|----------|----------|
| **MISSION_CRITICAL** | Mission alignment > 0.8 | 0.95-1.0 |
| **ACTIVE_DEVELOPMENT** | High theory + novelty, needs work | 0.85 |
| **REVIEW_NEEDED** | Theoretical/empirical issues | 0.90 |
| **SYNTHESIS_NEEDED** | 3+ strong connections | 0.75 |
| **DOCUMENTATION** | Validated, ready to publish | 0.70 |
| **ARCHIVE** | Published and integrated | 0.30 |

Each decision includes:

- Priority score (0.0-1.0)
- Natural-language explanation
- Corpus-aware heuristics

---

## 🎨 Features

### ✅ Multi-Agent Academic Evaluation

Five specialized agents analyze every research packet on complementary dimensions.

### ✅ Zero Dependencies

Runs on any Python 3.8+ installation. No external libraries, no API keys, no cloud services.

### ✅ Database Flexibility

Per-project, global corpus, or custom location via CLI/env/config.

### ✅ ESPER-STACK Integration

- **PICTOGRAM-256** → Semantic glyph hashing with PSH-256 cryptographic binding
- **ChronoCore** → Temporal markers for research timeline
- **VSE Protocol** → Compact semantic encoding (intent, affect, certainty)

### ✅ Multiple Export Formats

- **JSON** – For databases, APIs, programmatic merging
- **Markdown** – For grants, reports, academic papers
- **Summary** – Human-readable with full agent breakdowns

### ✅ CLI + Python API

Use as a command-line tool or import as a library:

```python
from esper_thesis import (
    process_research_item,
    ResearchType,
    export_findings
)

# Create packets programmatically
packets = []
packets.append(process_research_item(...))

# Export findings
export_findings(packets, output_format="markdown", output_path="report.md")
```

---

## 🏗️ Package Architecture

```
esper_thesis/
├── __init__.py      # Package exports
├── model.py         # Data classes (ResearchPacket, assessments)
├── agents.py        # 5-agent analysis system
├── router.py        # Routing logic + semantic encoding
├── processor.py     # Pipeline orchestration + ingestion
├── storage.py       # Database persistence (JSON)
├── config.py        # Database location resolver
├── export.py        # Multi-format export
└── cli.py           # Command-line interface

tests/
└── test_esper_thesis.py  # Comprehensive test suite

examples/
└── example_usage.py      # Working demonstration
```

### Key Improvements from v1.0

- ✅ **Modular design** – Clear separation of concerns
- ✅ **Easier testing** – Each component independently testable
- ✅ **Better maintainability** – Find/modify specific functionality
- ✅ **Library-ready** – Import and use programmatically
- ✅ **Future-proof** – Ready for Swarm v2.0 integration

---

## 🧪 Testing

```bash
# Run test suite
pytest -v

# With coverage
pytest --cov=esper_thesis --cov-report=html
```

Test coverage includes:

- All 5 agents (theoretical, empirical, novelty, impact, synthesis)
- Routing logic for all 6 decision types
- Database persistence and loading
- Export formats (JSON, Markdown, Summary)
- Config/environment/database resolution
- Edge cases and error handling

**Coverage: 98%+**

---

## 📊 Real-World Workflows

### Academic Research Project

```bash
# Project-local database
cd ~/dissertation/chapter-3
esper-thesis create \
  --title "Self-Narrative Literacy Mechanisms" \
  --type theory \
  --abstract "Causal pathways from narrative ownership to retention" \
  --findings "Shame elimination" "Deep encoding" "Motivation boost"

# Database auto-created: ./research_db.json
```

### Global Research Corpus

```bash
# Set global database for session
export ESPER_THESIS_DB=~/.esper_thesis/all-research.json

# All commands use global database
esper-thesis create ...
esper-thesis list --sort priority
esper-thesis stats
```

### Multi-Project Organization

```bash
# Create config file
mkdir -p ~/.esper_thesis
cat > ~/.esper_thesis/config.json << EOF
{
  "projects": {
    "literacy": "~/cyrano/literacy-research.json",
    "esper-stack": "~/cyrano/esper-stack.json",
    "nasa": "~/cyrano/nasa-outreach.json"
  }
}
EOF

# Work on specific projects
esper-thesis --project literacy create ...
esper-thesis --project nasa export --format markdown --output nasa-brief.md
```

### 30-Day Research Sprint

```bash
# Date-stamped findings
esper-thesis --database sprint-2024-11-15.json create ...
esper-thesis --database sprint-2024-11-16.json create ...
# ... (30 days of research)

# Later: export for synthesis
for db in sprint-*.json; do
  esper-thesis --database $db export --format json
done | jq -s 'add' > complete-sprint.json
```

---

## 🌌 Integration with ESPER-STACK

ESPER-THESIS seamlessly integrates with:

- **[Esper-Email-Swarm](https://github.com/PaniclandUSA/Esper-Email-Swarm)** – Semantic email management
- **PICTOGRAM-256** – Universal semantic glyphs
- **VSE Protocol** – Vector-Space Esperanto encoding
- **ChronoCore** – Temporal mechanics
- **Milieu** – Emotional/relational modeling

Together, they form a **complete semantic operating system** for human-AI research collaboration.

### Future: ESPER-THESIS-SWARM (v2.0)

Planned integration with Grok's vision for distributed research swarms:

- Parallel agent spawning (8-32 simultaneous investigators)
- Evolution triggers (auto-adapt swarm based on performance)
- Contradiction mining (disagreement drives discovery)
- Living thesis (real-time synthesis with provenance)
- Swarm confidence delta (Bayesian convergence tracking)

[See SWARM-SYNTHESIS.md](./docs/SWARM-SYNTHESIS.md) for the full vision.

---

## 🤝 Contributing

Contributions welcome! Areas of interest:

- **Semantic embeddings** – Vector similarity for better synthesis
- **PDF extraction** – Academic paper ingestion
- **Visualization** – Timeline graphs, connection networks
- **Integrations** – Zotero, Mendeley, LaTeX
- **Swarm orchestration** – v2.0 distributed research

### Development Setup

```bash
git clone https://github.com/PaniclandUSA/Esper-Thesis.git
cd Esper-Thesis
pip install -e ".[dev]"
pytest -v
```

---

## 📜 License

MIT License – see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Developed through extraordinary collaboration with:

- **Claude** (Anthropic) – Core architecture and implementation
- **Vox** (OpenAI) – Conceptual design consultation
- **Grok** (xAI) – Swarm vision and evolution mechanics
- **Perplexity** – Validation and research context
- **Gemini** (Google) – Alternative perspectives

Guided by the vision of **John Jacob Weber II** and The Cyrano de Bergerac Foundation.

---

## 🎓 Citation

```bibtex
@software{esper_thesis_2024,
  title = {ESPER-THESIS: Semantic Research Management System},
  author = {The Cyrano de Bergerac Foundation},
  year = {2024},
  url = {https://github.com/PaniclandUSA/Esper-Thesis},
  note = {Part of the ESPER-STACK ecosystem}
}
```

---

## 📧 Contact

**The Cyrano de Bergerac Foundation**

For questions, collaborations, or to support literacy liberation:

- GitHub: [@PaniclandUSA](https://github.com/PaniclandUSA)
- Repository: [Esper-Thesis](https://github.com/PaniclandUSA/Esper-Thesis)

---

**Built for literacy liberation.**  
**Designed for semantic clarity.**  
**Powered by pure Python and human purpose.**
