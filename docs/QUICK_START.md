# ESPER-THESIS Quick Start

**Get from zero to first research packet in 5 minutes.**

---

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install esper-thesis
```

### From Source

```bash
git clone https://github.com/PaniclandUSA/Esper-Thesis.git
cd Esper-Thesis
pip install -e .
```

### Verify Installation

```bash
esper-thesis --version
# Output: esper-thesis 1.0.0
```

---

## 🚀 Create Your First Research Packet

### Example 1: Theory Research

```bash
esper-thesis create \
  --title "PICTOGRAM-256: Universal Semantic Communication" \
  --type theory \
  --abstract "A complete 256-glyph system with cryptographic binding for semantic interoperability" \
  --findings "8-bit isomorphism" "Geometric universals" "AI-validated reconstruction"
```

**Output:**
```
✓ Created: a3f7b921
  Title: PICTOGRAM-256: Universal Semantic Communication
  Type: theory
  Routing: active_development
  Priority: 0.87
  Database: ./research_db.json
```

### Example 2: Validation Research

```bash
esper-thesis create \
  --title "Self-Narrative Literacy Field Test" \
  --type validation \
  --abstract "Field test of self-narrative approach with 50 adult learners" \
  --findings "85% retention improvement" "Zero dropout rate" "100% comprehension reported"
```

**Output:**
```
✓ Created: b4e2c8a7
  Title: Self-Narrative Literacy Field Test
  Type: validation
  Routing: mission_critical
  Priority: 0.96
  Database: ./research_db.json
```

---

## 📋 List Your Research

### View All Packets (by priority)

```bash
esper-thesis list --sort priority
```

**Output:**
```
Research Packets (2 shown):

[b4e2c8a7] Self-Narrative Literacy Field Test
  Type: validation | Priority: 0.96

[a3f7b921] PICTOGRAM-256: Universal Semantic Communication
  Type: theory | Priority: 0.87
```

### Filter by Type

```bash
esper-thesis list --type validation --limit 5
```

---

## 📊 View Packet Details

```bash
esper-thesis show b4e2c8a7
```

**Output:**
```
Research Packet: b4e2c8a7
==================================================

Title: Self-Narrative Literacy Field Test
Type: validation
Status: draft

Abstract:
Field test of self-narrative approach with 50 adult learners

Key Findings:
  • 85% retention improvement
  • Zero dropout rate
  • 100% comprehension reported

Assessment:
  Theoretical: 0.82 (strong conceptual foundation)
  Empirical: 0.91 (high validation support)
  Novelty: 0.78 (significant originality)
  Impact: 0.96 (mission-critical alignment)

Routing: mission_critical
Priority: 0.96

Created: 2024-12-06 14:23:45
Database: ./research_db.json
```

---

## 📤 Export Research

### Markdown Report

```bash
esper-thesis export --format markdown --output findings.md
```

**Creates `findings.md`:**
```markdown
# Research Findings

## Self-Narrative Literacy Field Test
**Type**: validation
**Priority**: 0.96

Field test of self-narrative approach with 50 adult learners

**Key Findings**:
- 85% retention improvement
- Zero dropout rate
- 100% comprehension reported

---

## PICTOGRAM-256: Universal Semantic Communication
**Type**: theory
**Priority**: 0.87

A complete 256-glyph system with cryptographic binding...
```

### JSON Export

```bash
esper-thesis export --format json --output research.json
```

### Filter Exports

```bash
# Only high-priority packets
esper-thesis export --format markdown --min-priority 0.9 --output high_priority.md

# Only validation research
esper-thesis export --format json --filter-type validation --output validations.json
```

---

## 📈 Database Statistics

```bash
esper-thesis stats
```

**Output:**
```
============================================================
ESPER-THESIS Statistics
============================================================

Total Packets: 2

By Type:
  validation     :   1
  theory         :   1

By Routing:
  mission_critical   :   1
  active_development :   1

Average Priority: 0.92

Top 3 Priorities:
  1. [b4e2c8a7] Self-Narrative Literacy Field Test (0.96)
  2. [a3f7b921] PICTOGRAM-256 (0.87)
```

---

## 🔧 Configuration

### Use Different Database

```bash
# Explicit path
esper-thesis --database ~/research/global.json create ...

# Environment variable
export ESPER_THESIS_DB=~/research/main.json
esper-thesis create ...
```

### Named Projects

Create `~/.esper_thesis/config.json`:

```json
{
  "projects": {
    "literacy": "~/projects/literacy/research.json",
    "nasa": "~/projects/nasa/research.json",
    "esper-stack": "~/esper/research.json"
  }
}
```

Use projects:

```bash
esper-thesis --project literacy create \
  --title "Reading Retention Study" \
  --type validation \
  --abstract "..." \
  --findings "..."
```

### Show Configuration

```bash
esper-thesis config show
```

---

## 🐍 Python API Quick Start

### Basic Usage

```python
from esper_thesis import process_research_item, ResearchType

# Create packet
packet = process_research_item(
    title="VSE Protocol Validation",
    abstract="Validated Vector-Space Esperanto through 5-AI Turing Tour",
    key_findings=[
        "95% semantic reconstruction accuracy",
        "40% token compression achieved",
        "Zero training on target concepts"
    ],
    research_type=ResearchType.VALIDATION,
    source="ai_experiment"
)

# Access results
print(f"Packet ID: {packet.packet_id}")
print(f"Priority: {packet.priority_score:.2f}")
print(f"Routing: {packet.routing_decision.value}")
print(f"Theoretical score: {packet.theoretical.score:.2f}")
```

### Load and Query Database

```python
from esper_thesis.storage import load_database

# Load packets
packets = load_database("research_db.json")

# Filter high-priority
high_priority = [p for p in packets if p.priority_score > 0.9]

print(f"Found {len(high_priority)} high-priority packets")

for packet in high_priority:
    print(f"  - {packet.title} ({packet.priority_score:.2f})")
```

---

## 🎯 Common Workflows

### Academic Literature Review

```bash
# 1. Create packets for each paper
esper-thesis create \
  --title "Paper Title" \
  --type theory \
  --abstract "Paper abstract" \
  --findings "Key finding 1" "Key finding 2"

# 2. Track validation studies
esper-thesis create \
  --type validation \
  --title "Replication Study" \
  --abstract "..." \
  --findings "..."

# 3. Export organized findings
esper-thesis export --format markdown --output literature_review.md
```

### Field Research Documentation

```bash
# 1. Create insights from field notes
esper-thesis create \
  --type insight \
  --title "Classroom Observation: Day 5" \
  --abstract "Students respond better to story-based approach" \
  --findings "Engagement increased" "Questions more thoughtful"

# 2. Create validation from outcomes
esper-thesis create \
  --type validation \
  --title "Week 1 Assessment Results" \
  --abstract "End of week 1 comprehension test" \
  --findings "Average 78% improvement" "All students passed"

# 3. View progress
esper-thesis stats
```

### Grant Proposal Research

```bash
# 1. Gather all research
esper-thesis list --sort priority

# 2. Export high-priority findings
esper-thesis export \
  --format markdown \
  --min-priority 0.8 \
  --output grant_evidence.md

# 3. Get statistics for proposal
esper-thesis stats
```

---

## 💡 Tips & Best Practices

### Naming Conventions
- **Title**: Descriptive but concise (< 100 chars)
- **Abstract**: 1-3 sentences summarizing the work
- **Findings**: Short, specific claims (not paragraphs)

### Research Types
- `theory`: Conceptual frameworks, models
- `validation`: Empirical tests, experiments
- `application`: Real-world implementations
- `insight`: Field observations, eureka moments
- `synthesis`: Meta-analysis, integration
- `question`: Open inquiries
- `breakthrough`: Paradigm shifts

### Database Organization
- **Single project**: Use default `./research_db.json`
- **Multiple projects**: Use `--project` with config file
- **Global corpus**: Set `ESPER_THESIS_DB` environment variable

### Status Progression
```bash
# Initially created
Status: draft

# After validation
esper-thesis update PACKET_ID --status validated

# After publication/integration
esper-thesis update PACKET_ID --status published
```

---

## 🔍 Troubleshooting

### "Command not found: esper-thesis"

Ensure package is installed:
```bash
pip install esper-thesis
# Or for development:
pip install -e .
```

### "Database file not found"

Check current directory or specify path:
```bash
esper-thesis --database ~/research.json list
```

### Import errors in Python

Ensure package is importable:
```python
import esper_thesis
print(esper_thesis.__version__)
```

---

## 📚 Next Steps

Now that you've created your first packets:

- **[Complete CLI Reference](CLI_REFERENCE.md)** - All commands and options
- **[Python API Guide](API.md)** - Library usage and advanced features
- **[Data Model](DATA_MODEL.md)** - Understanding packet structure
- **[Architecture](ARCHITECTURE.md)** - How the system works
- **[Provenance Guide](PROVENANCE.md)** - Trust and citation practices

---

## 🎓 Example: 30-Day Research Sprint

See [examples/30_day_sprint.py](../examples/30_day_sprint.py) for complete workflow demonstrating:
- Creating 30 research packets over time
- Building synthesis connections
- Tracking mission-critical research
- Exporting for publication

---

**You're ready to organize research for literacy liberation!** 🚀📚
