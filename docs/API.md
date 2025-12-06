# ESPER-THESIS Python API

Complete Python library reference for programmatic usage.

---

## Installation

```bash
pip install esper-thesis
```

---

## Quick Start

### Basic Usage

```python
from esper_thesis import process_research_item, ResearchType

# Create research packet
packet = process_research_item(
    title="PICTOGRAM-256 Validation",
    abstract="AI system reconstructed philosophy from geometric glyphs",
    key_findings=[
        "95% semantic reconstruction accuracy",
        "Zero training on target concepts",
        "5-AI independent validation"
    ],
    research_type=ResearchType.VALIDATION,
    source="ai_experiment"
)

# Access results
print(f"Packet ID: {packet.packet_id}")
print(f"Priority: {packet.priority_score:.2f}")
print(f"Routing: {packet.routing_decision.value}")
```

**Output:**
```
Packet ID: a3f7b921
Priority: 0.91
Routing: mission_critical
```

---

## Core API

### `process_research_item()`

Main entry point for creating research packets with full analysis.

**Signature:**
```python
def process_research_item(
    title: str,
    abstract: str,
    key_findings: List[str],
    research_type: ResearchType,
    source: str = "manual",
    methodology: str = "",
    tags: Optional[List[str]] = None
) -> ResearchPacket
```

**Parameters:**
- `title` (str) - Research title
- `abstract` (str) - Brief description
- `key_findings` (List[str]) - Main discoveries
- `research_type` (ResearchType) - Type enum
- `source` (str, optional) - Source type (default: "manual")
- `methodology` (str, optional) - Research methodology
- `tags` (List[str], optional) - Organization tags

**Returns:**
- `ResearchPacket` - Complete packet with all assessments

**Example:**
```python
from esper_thesis import process_research_item, ResearchType

packet = process_research_item(
    title="Self-Narrative Literacy Pilot",
    abstract="50-learner field test of story-based approach",
    key_findings=[
        "85% retention improvement",
        "Zero dropout rate",
        "100% comprehension reported"
    ],
    research_type=ResearchType.VALIDATION,
    source="field_study",
    methodology="Randomized controlled trial with pre/post assessment",
    tags=["literacy", "field-test", "pilot"]
)

print(f"Mission alignment: {packet.impact.mission_alignment:.2f}")
# Output: Mission alignment: 0.96
```

---

## Data Models

### `ResearchPacket`

Core data structure for research units.

**Fields:**

```python
@dataclass
class ResearchPacket:
    packet_id: str              # 8-character unique ID
    title: str                  # Research title
    research_type: ResearchType # Type enum
    abstract: str               # Brief description
    key_findings: List[str]     # Main discoveries
    
    # Multi-agent assessments
    theoretical: TheoreticalAssessment
    empirical: EmpiricalAssessment
    novelty: NoveltyAssessment
    impact: ImpactAssessment
    synthesis: SynthesisAssessment
    
    # Routing
    routing_decision: RoutingDecision
    priority_score: float       # 0.0-1.0
    routing_explanation: str
    
    # ESPER-STACK encoding
    pictogram_hash: str         # 3-char glyph
    chrono_marker: str          # Temporal marker
    vse_encoding: Dict[str, Any]
    
    # Metadata
    timestamp: str              # ISO 8601
    source: str                 # Source type
    methodology: str            # Research method
    tags: List[str]             # Organization tags
    status: str                 # Lifecycle status
```

**Example:**
```python
# Access assessments
print(f"Theoretical score: {packet.theoretical.score:.2f}")
print(f"Logical consistency: {packet.theoretical.logical_consistency:.2f}")
print(f"Breakthrough potential: {packet.theoretical.breakthrough_potential:.2f}")

# Access routing
print(f"Decision: {packet.routing_decision.value}")
print(f"Priority: {packet.priority_score:.2f}")
print(f"Explanation: {packet.routing_explanation}")

# Access ESPER-STACK
print(f"PICTOGRAM: {packet.pictogram_hash}")
print(f"ChronoCore: {packet.chrono_marker}")
print(f"VSE: {packet.vse_encoding}")
```

### `ResearchType` Enum

Research categorization.

```python
class ResearchType(Enum):
    THEORY = "theory"
    VALIDATION = "validation"
    APPLICATION = "application"
    INSIGHT = "insight"
    SYNTHESIS = "synthesis"
    QUESTION = "question"
    BREAKTHROUGH = "breakthrough"
```

**Usage:**
```python
from esper_thesis import ResearchType

# By enum
packet = process_research_item(
    ...,
    research_type=ResearchType.VALIDATION
)

# By string (auto-converted)
research_type=ResearchType.THEORY
print(research_type.value)  # "theory"
```

### `RoutingDecision` Enum

Routing categories.

```python
class RoutingDecision(Enum):
    MISSION_CRITICAL = "mission_critical"
    ACTIVE_DEVELOPMENT = "active_development"
    SYNTHESIS_NEEDED = "synthesis_needed"
    REVIEW_NEEDED = "review_needed"
    DOCUMENTATION = "documentation"
    ARCHIVE = "archive"
```

---

## Agent Functions

Access individual agent assessments directly.

### `theoretical_agent()`

Assess conceptual coherence and breakthrough potential.

**Signature:**
```python
def theoretical_agent(
    title: str,
    abstract: str,
    key_findings: List[str],
    methodology: str
) -> TheoreticalAssessment
```

**Returns:**
```python
@dataclass
class TheoreticalAssessment:
    score: float                    # Overall 0.0-1.0
    logical_consistency: float      # Internal coherence
    conceptual_clarity: float       # Clear definitions
    foundation_strength: float      # Builds on prior work
    breakthrough_potential: float   # Paradigm shift likelihood
    dependencies: List[str]         # Required prior knowledge
```

**Example:**
```python
from esper_thesis.agents import theoretical_agent

assessment = theoretical_agent(
    title="Universal Semantic Glyphs",
    abstract="256-glyph system with geometric universals",
    key_findings=["8-bit isomorphism", "Cryptographic binding"],
    methodology="Theoretical construction with AI validation"
)

print(f"Breakthrough potential: {assessment.breakthrough_potential:.2f}")
print(f"Dependencies: {assessment.dependencies}")
```

### `empirical_agent()`

Track validation evidence and reproducibility.

**Signature:**
```python
def empirical_agent(
    title: str,
    abstract: str,
    key_findings: List[str],
    methodology: str,
    research_type: ResearchType
) -> EmpiricalAssessment
```

**Returns:**
```python
@dataclass
class EmpiricalAssessment:
    support_level: float            # 0.0-1.0
    validation_type: str            # Type of validation
    reproducible: bool              # Can be replicated
    evidence_sources: List[str]     # Evidence references
```

**Example:**
```python
from esper_thesis.agents import empirical_agent

assessment = empirical_agent(
    title="Field Test Results",
    abstract="50-learner pilot study",
    key_findings=["85% improvement", "Zero dropout"],
    methodology="RCT with pre/post assessment",
    research_type=ResearchType.VALIDATION
)

print(f"Support level: {assessment.support_level:.2f}")
print(f"Reproducible: {assessment.reproducible}")
```

### `novelty_agent()`

Evaluate originality and paradigm shift potential.

**Signature:**
```python
def novelty_agent(
    title: str,
    abstract: str,
    key_findings: List[str],
    research_type: ResearchType
) -> NoveltyAssessment
```

**Returns:**
```python
@dataclass
class NoveltyAssessment:
    score: float                    # Overall originality 0.0-1.0
    originality_score: float        # Uniqueness
    paradigm_shift: bool            # Revolutionary potential
    unique_contributions: List[str] # Novel aspects
```

### `impact_agent()`

Measure significance and mission alignment.

**Signature:**
```python
def impact_agent(
    title: str,
    abstract: str,
    key_findings: List[str],
    research_type: ResearchType
) -> ImpactAssessment
```

**Returns:**
```python
@dataclass
class ImpactAssessment:
    potential: float                # Overall impact 0.0-1.0
    academic_impact: float          # Research significance
    industry_application: float     # Practical value
    mission_alignment: float        # Literacy liberation alignment
```

### `synthesis_agent()`

Discover connections to other research.

**Signature:**
```python
def synthesis_agent(
    packet: ResearchPacket,
    existing_packets: List[ResearchPacket]
) -> SynthesisAssessment
```

**Returns:**
```python
@dataclass
class SynthesisAssessment:
    connections: List[str]          # Related packet IDs
    themes: List[str]               # Emerging themes
    contradictions: List[str]       # Conflicting packets
```

---

## Storage Functions

### `load_database()`

Load research packets from JSON file.

**Signature:**
```python
def load_database(db_path: str = "research_db.json") -> List[ResearchPacket]
```

**Parameters:**
- `db_path` (str) - Database file path

**Returns:**
- `List[ResearchPacket]` - All packets

**Example:**
```python
from esper_thesis.storage import load_database

# Load default database
packets = load_database()

# Load specific database
packets = load_database("~/research/global.json")

print(f"Loaded {len(packets)} packets")
```

### `save_database()`

Save research packets to JSON file.

**Signature:**
```python
def save_database(
    packets: List[ResearchPacket],
    db_path: str = "research_db.json"
) -> None
```

**Parameters:**
- `packets` (List[ResearchPacket]) - Packets to save
- `db_path` (str) - Database file path

**Example:**
```python
from esper_thesis.storage import save_database

# Create new packet
packet = process_research_item(...)

# Load existing
packets = load_database()

# Add and save
packets.append(packet)
save_database(packets)
```

---

## Export Functions

### `export_findings()`

Export research packets in various formats.

**Signature:**
```python
def export_findings(
    packets: List[ResearchPacket],
    output_format: str = "json",
    output_path: Optional[str] = None,
    min_priority: float = 0.0
) -> str
```

**Parameters:**
- `packets` (List[ResearchPacket]) - Packets to export
- `output_format` (str) - Format: "json", "markdown", "summary"
- `output_path` (str, optional) - Output file path
- `min_priority` (float) - Minimum priority filter

**Returns:**
- `str` - Formatted output (if no output_path)

**Example:**
```python
from esper_thesis import export_findings, load_database

packets = load_database()

# Markdown report
export_findings(
    packets,
    output_format="markdown",
    output_path="findings.md"
)

# High-priority JSON
high_priority = export_findings(
    packets,
    output_format="json",
    min_priority=0.8
)
print(high_priority)
```

---

## Configuration Functions

### `get_database_path()`

Resolve database path using 4-level cascade.

**Signature:**
```python
def get_database_path(
    cli_path: Optional[str] = None,
    project: Optional[str] = None
) -> str
```

**Parameters:**
- `cli_path` (str, optional) - Explicit path
- `project` (str, optional) - Named project

**Returns:**
- `str` - Resolved database path

**Resolution Order:**
1. `cli_path` argument
2. `ESPER_THESIS_DB` environment variable
3. Config file project
4. Default: `./research_db.json`

**Example:**
```python
from esper_thesis.config import get_database_path
import os

# Explicit path (highest priority)
path = get_database_path(cli_path="~/research.json")
# Returns: ~/research.json

# Environment variable
os.environ["ESPER_THESIS_DB"] = "~/global.json"
path = get_database_path()
# Returns: ~/global.json

# Named project (requires config file)
path = get_database_path(project="literacy")
# Returns: ~/projects/literacy/research.json

# Default
path = get_database_path()
# Returns: ./research_db.json
```

---

## Advanced Usage

### Custom Analysis Workflow

```python
from esper_thesis import process_research_item, load_database, save_database
from esper_thesis.agents import theoretical_agent, empirical_agent

# Create packet with custom analysis
packet = process_research_item(
    title="Custom Research",
    abstract="...",
    key_findings=["..."],
    research_type=ResearchType.THEORY
)

# Run additional analysis
theoretical = theoretical_agent(
    title=packet.title,
    abstract=packet.abstract,
    key_findings=packet.key_findings,
    methodology=packet.methodology
)

# Custom logic
if theoretical.breakthrough_potential > 0.9:
    print("BREAKTHROUGH DETECTED!")
    packet.tags.append("breakthrough")

# Save with custom modifications
packets = load_database()
packets.append(packet)
save_database(packets)
```

### Filtering and Querying

```python
from esper_thesis import load_database, ResearchType, RoutingDecision

packets = load_database()

# High-priority packets
high_priority = [p for p in packets if p.priority_score > 0.9]

# Mission-critical routing
mission_critical = [
    p for p in packets 
    if p.routing_decision == RoutingDecision.MISSION_CRITICAL
]

# Validation research
validations = [
    p for p in packets
    if p.research_type == ResearchType.VALIDATION
]

# Published papers
published = [p for p in packets if p.status == "published"]

# Complex query
breakthrough_validations = [
    p for p in packets
    if p.research_type == ResearchType.VALIDATION
    and p.novelty.paradigm_shift
    and p.priority_score > 0.85
]

print(f"Found {len(breakthrough_validations)} breakthrough validations")
```

### Batch Processing

```python
from esper_thesis import process_research_item, save_database, ResearchType
import json

# Load data from JSON
with open("research_data.json") as f:
    data = json.load(f)

# Process batch
packets = []
for item in data:
    packet = process_research_item(
        title=item["title"],
        abstract=item["abstract"],
        key_findings=item["findings"],
        research_type=ResearchType[item["type"].upper()]
    )
    packets.append(packet)

# Save all
save_database(packets, "batch_results.json")
print(f"Processed {len(packets)} packets")
```

### Custom Routing Logic

```python
from esper_thesis import ResearchPacket, process_research_item
from esper_thesis.router import route_research

def custom_router(packet: ResearchPacket):
    """Custom routing with project-specific rules."""
    
    # Get baseline routing
    routing, priority, explanation = route_research(packet)
    
    # Boost NASA-related research
    if "nasa" in packet.title.lower() or "nasa" in packet.tags:
        priority = min(1.0, priority + 0.15)
        explanation += " [NASA project boost applied]"
    
    # Flag contradictions
    if len(packet.synthesis.contradictions) > 0:
        routing = RoutingDecision.REVIEW_NEEDED
        priority = max(0.85, priority)
        explanation += " [Contradictions detected]"
    
    return routing, priority, explanation

# Use custom router
packet = process_research_item(...)
routing, priority, explanation = custom_router(packet)
print(f"Custom routing: {routing.value} ({priority:.2f})")
```

### Analysis Pipeline

```python
from esper_thesis import load_database
from collections import Counter

packets = load_database()

# Statistics
total = len(packets)
avg_priority = sum(p.priority_score for p in packets) / total

type_counts = Counter(p.research_type.value for p in packets)
routing_counts = Counter(p.routing_decision.value for p in packets)

# Find patterns
high_impact = [p for p in packets if p.impact.potential > 0.9]
needs_validation = [
    p for p in packets
    if p.empirical.support_level < 0.5
    and p.theoretical.score > 0.8
]

print(f"Total packets: {total}")
print(f"Average priority: {avg_priority:.2f}")
print(f"High impact: {len(high_impact)}")
print(f"Needs validation: {len(needs_validation)}")
print(f"\nBy type: {dict(type_counts)}")
print(f"By routing: {dict(routing_counts)}")
```

---

## Error Handling

### Common Exceptions

```python
from esper_thesis import load_database, save_database
from esper_thesis.storage import DatabaseError

try:
    packets = load_database("nonexistent.json")
except FileNotFoundError:
    print("Database not found, creating new")
    packets = []

try:
    save_database(packets, "/readonly/path.json")
except PermissionError:
    print("Cannot write to read-only location")

try:
    packets = load_database("corrupt.json")
except DatabaseError as e:
    print(f"Database error: {e}")
```

---

## Type Hints

All functions include complete type hints:

```python
from typing import List, Optional, Dict, Any
from esper_thesis import ResearchPacket, ResearchType

def my_analysis(
    packets: List[ResearchPacket],
    min_priority: float = 0.0
) -> Dict[str, Any]:
    """Custom analysis with type safety."""
    
    results: Dict[str, Any] = {
        "total": len(packets),
        "high_priority": []
    }
    
    for packet in packets:
        if packet.priority_score >= min_priority:
            results["high_priority"].append({
                "id": packet.packet_id,
                "title": packet.title,
                "priority": packet.priority_score
            })
    
    return results
```

---

## Integration Examples

### Jupyter Notebook

```python
# notebook.ipynb
import esper_thesis as et
import pandas as pd
import matplotlib.pyplot as plt

# Load research
packets = et.load_database()

# Create DataFrame
df = pd.DataFrame([{
    "id": p.packet_id,
    "title": p.title,
    "type": p.research_type.value,
    "priority": p.priority_score,
    "theoretical": p.theoretical.score,
    "empirical": p.empirical.support_level,
    "novelty": p.novelty.score,
    "impact": p.impact.potential
} for p in packets])

# Visualize
df.plot.scatter(x="theoretical", y="empirical", s=df["priority"]*100)
plt.title("Research Landscape")
plt.show()

# Summary stats
print(df.describe())
```

### Flask API

```python
# app.py
from flask import Flask, jsonify, request
from esper_thesis import process_research_item, load_database, ResearchType

app = Flask(__name__)

@app.route("/api/packets", methods=["GET"])
def list_packets():
    packets = load_database()
    return jsonify([{
        "id": p.packet_id,
        "title": p.title,
        "priority": p.priority_score
    } for p in packets])

@app.route("/api/packets", methods=["POST"])
def create_packet():
    data = request.json
    packet = process_research_item(
        title=data["title"],
        abstract=data["abstract"],
        key_findings=data["findings"],
        research_type=ResearchType[data["type"].upper()]
    )
    return jsonify({"id": packet.packet_id}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Best Practices

### Idiomatic Usage

```python
# ✅ Good: Use ResearchType enum
packet = process_research_item(
    ...,
    research_type=ResearchType.VALIDATION
)

# ❌ Bad: String literals
packet = process_research_item(
    ...,
    research_type="validation"  # Will work but not type-safe
)

# ✅ Good: Filter with list comprehensions
high_priority = [p for p in packets if p.priority_score > 0.9]

# ❌ Bad: Manual loops
high_priority = []
for p in packets:
    if p.priority_score > 0.9:
        high_priority.append(p)

# ✅ Good: Use context for file operations
with open("output.json", "w") as f:
    json.dump(packets, f)

# ❌ Bad: Manual file handling
f = open("output.json", "w")
json.dump(packets, f)
f.close()
```

---

**Complete API documentation. For CLI usage, see [CLI_REFERENCE.md](CLI_REFERENCE.md).**
