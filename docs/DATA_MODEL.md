# ESPER-THESIS Data Model

Complete schema documentation for research packets.

---

## Research Packet Schema v1.0

### Overview

Every research packet is a structured semantic unit with cryptographic binding and multi-agent assessment.

---

## Core Fields (Required)

| Field | Type | Description | Example | Constraints |
|-------|------|-------------|---------|-------------|
| `packet_id` | string | Unique identifier | `a3f7b921` | 8 chars, hex |
| `title` | string | Research title | "PICTOGRAM-256 Architecture" | 1-200 chars |
| `research_type` | enum | Type of contribution | `theory` | See ResearchType |
| `abstract` | string | Brief description | "Complete 256-glyph system..." | 10-1000 chars |
| `key_findings` | list[str] | Main discoveries | ["8-bit isomorphism", ...] | 1-20 items |

**Validation Rules:**
- `packet_id`: Generated automatically via PSH-256 hash of title+timestamp
- `title`: Must be unique within database
- `key_findings`: Each finding 5-500 characters

---

## Metadata (Auto-generated)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `timestamp` | string | Creation time (ISO 8601) | `2024-12-06T14:30:45Z` |
| `source` | string | Source type | `manual`, `conversation`, `document` |
| `methodology` | string | Research method | "Randomized controlled trial" |
| `tags` | list[str] | Organization tags | ["literacy", "pilot"] |
| `status` | string | Lifecycle status | `draft`, `validated`, `published` |

**Default Values:**
- `source`: "manual"
- `methodology`: "" (empty string)
- `tags`: [] (empty list)
- `status`: "draft"

---

## Multi-Agent Assessment

### Theoretical Assessment

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `score` | float | 0.0-1.0 | Overall theoretical strength |
| `logical_consistency` | float | 0.0-1.0 | Internal coherence |
| `conceptual_clarity` | float | 0.0-1.0 | Clear definitions |
| `foundation_strength` | float | 0.0-1.0 | Builds on prior work |
| `breakthrough_potential` | float | 0.0-1.0 | Paradigm shift likelihood |
| `dependencies` | list[str] | - | Required prior knowledge |

**Calculation:**
```python
score = (logical_consistency + conceptual_clarity + 
         foundation_strength + breakthrough_potential) / 4
```

**Interpretation:**
- **0.9-1.0**: Exceptional theoretical foundation
- **0.7-0.9**: Strong conceptual basis
- **0.5-0.7**: Adequate theory
- **< 0.5**: Needs theoretical development

### Empirical Assessment

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `support_level` | float | 0.0-1.0 | Validation strength |
| `validation_type` | string | - | Type of validation |
| `reproducible` | bool | - | Can be replicated |
| `evidence_sources` | list[str] | - | Evidence references |

**Validation Types:**
- `theoretical`: No empirical validation yet
- `preliminary`: Initial testing
- `pilot`: Small-scale study
- `validated`: Full validation
- `replicated`: Independently reproduced

**Support Level Thresholds:**
- `validation` research: 0.7-1.0
- `application` research: 0.6-0.9
- `theory` research: 0.3-0.7 (lower acceptable)

### Novelty Assessment

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `score` | float | 0.0-1.0 | Overall originality |
| `originality_score` | float | 0.0-1.0 | Uniqueness |
| `paradigm_shift` | bool | - | Revolutionary potential |
| `unique_contributions` | list[str] | - | Novel aspects |

**Paradigm Shift Detection:**
- Keywords: "first", "never", "paradigm", "breakthrough", "revolutionary"
- Breakthrough research type automatically triggers
- Multiple unique contributions (3+) suggest high novelty

### Impact Assessment

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `potential` | float | 0.0-1.0 | Overall impact |
| `academic_impact` | float | 0.0-1.0 | Research significance |
| `industry_application` | float | 0.0-1.0 | Practical value |
| `mission_alignment` | float | 0.0-1.0 | Literacy liberation fit |

**Mission Alignment Keywords:**
- High (0.8-1.0): literacy, reading, learner, education, shame elimination
- Medium (0.5-0.8): teaching, learning, comprehension, retention
- Low (0.0-0.5): Other topics

**Calculation:**
```python
potential = (academic_impact + industry_application + mission_alignment) / 3
```

### Synthesis Assessment

| Field | Type | Description |
|-------|------|-------------|
| `connections` | list[str] | Related packet IDs (keyword overlap) |
| `themes` | list[str] | Emerging themes across connections |
| `contradictions` | list[str] | Packets with opposing claims |

**Connection Detection:**
- Shared keywords in titles/abstracts/findings
- Common tags
- Similar research types
- Chronological proximity

---

## Routing Decision

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| `routing_decision` | enum | Destination category | See RoutingDecision |
| `priority_score` | float | Overall priority | 0.0-1.0 |
| `routing_explanation` | string | Human-readable explanation | 50-500 chars |

### Routing Decisions

| Value | Priority Range | Meaning | Typical Triggers |
|-------|---------------|---------|------------------|
| `mission_critical` | 0.95-1.0 | Direct literacy impact | High mission_alignment, validation |
| `active_development` | 0.80-0.90 | High potential, needs work | Strong theory, preliminary validation |
| `synthesis_needed` | 0.70-0.80 | Multiple connections | 3+ connections, emerging themes |
| `review_needed` | 0.85-0.95 | Issues to address | High theory, low empirical |
| `documentation` | 0.65-0.75 | Ready for publication | Validated, clear, reproducible |
| `archive` | 0.20-0.40 | Complete, integrated | Published status |

### Priority Calculation

```python
priority = (
    theoretical.score * 0.20 +
    empirical.support_level * 0.20 +
    novelty.score * 0.20 +
    impact.potential * 0.30 +
    mission_alignment * 0.10
)

# Bonuses
if novelty.paradigm_shift:
    priority += 0.05
if research_type == BREAKTHROUGH:
    priority += 0.10
if len(synthesis.connections) >= 5:
    priority += 0.05

# Clamp to [0, 1]
priority = min(1.0, max(0.0, priority))
```

---

## ESPER-STACK Integration

### PICTOGRAM-256 Encoding

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `pictogram_hash` | string | 3-character semantic glyph | `T8A` |

**Generation:**
```python
# PSH-256 hash of title
hash_bytes = hashlib.sha256(title.encode()).digest()
# Map to PICTOGRAM-256 space
glyph = map_to_pictogram(hash_bytes[:3])
```

**Properties:**
- **Cryptographically bound**: Same title always produces same glyph
- **Collision resistant**: PSH-256 foundation
- **Semantic**: Glyphs have geometric meaning

### ChronoCore Temporal Marker

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `chrono_marker` | string | Temporal marker | `2024-12-06_THEORY_001` |

**Format:**
```
YYYY-MM-DD_TYPE_SEQUENCE
```

**Components:**
- `YYYY-MM-DD`: Creation date
- `TYPE`: Research type (uppercase)
- `SEQUENCE`: Daily counter per type

### VSE Protocol Encoding

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `vse_encoding` | dict | Semantic encoding | `{intent: "theory", affect: 0.75, certainty: 0.87}` |

**Schema:**
```python
{
    "intent": str,           # Research type value
    "affect": float,         # Emotional valence (0.0-1.0)
    "certainty": float,      # Priority score
    "context": list[str]     # Tags
}
```

---

## ResearchType Enum

| Value | Description | When to Use | Typical Priority |
|-------|-------------|-------------|------------------|
| `theory` | Conceptual frameworks | Proposing new understanding | 0.6-0.9 |
| `validation` | Empirical tests | Proving/disproving claims | 0.7-1.0 |
| `application` | Real-world implementations | Building actual tools | 0.6-0.85 |
| `insight` | Observations, connections | Field notes, eureka moments | 0.5-0.75 |
| `synthesis` | Integration across findings | Meta-analysis | 0.65-0.85 |
| `question` | Open research inquiries | Framing problems | 0.4-0.7 |
| `breakthrough` | Paradigm shifts | Revolutionary discoveries | 0.85-1.0 |

---

## Status Lifecycle

```
draft ──────> validated ──────> published
  │                                 │
  └─────────────────────────────────┘
         (can revert to draft)
```

| Status | Meaning | Typical Journey |
|--------|---------|-----------------|
| `draft` | Initially created, undergoing development | All packets start here |
| `validated` | Empirical evidence gathered, reviewed | After field tests, peer review |
| `published` | Externally shared, cited, integrated | Papers, blogs, grants |

**Progression Triggers:**
- `draft → validated`: Empirical support > 0.7, peer review
- `validated → published`: External sharing, DOI/URL added
- `published → draft`: Major revisions needed

---

## Schema Versioning

### Current: v1.0

**Future Compatibility:**
- All packets include implicit `schema_version: "1.0"`
- Migration scripts for schema evolution
- Backward compatibility maintained

### Planned v1.5 Additions

- `embedding` (optional): Semantic vector
- `vector_id` (optional): Vector store reference
- `contradicts` (list[str]): Explicit contradiction links
- `supports` (list[str]): Explicit support links

---

## Validation Rules

### Title
- Length: 1-200 characters
- Must be unique within database
- Recommended: Descriptive but concise

### Abstract
- Length: 10-1000 characters
- Should summarize key contribution
- Avoid excessive jargon

### Key Findings
- Count: 1-20 findings
- Length per finding: 5-500 characters
- Should be specific, measurable claims

### Research Type
- Must be valid ResearchType enum value
- Impacts routing and assessment weights

### Status
- Must be: "draft", "validated", or "published"
- Default: "draft"

---

## Example Complete Packet

```json
{
  "packet_id": "a3f7b921",
  "title": "Self-Narrative Literacy Pilot Study",
  "research_type": "validation",
  "abstract": "Field test of self-narrative approach with 50 adult learners over 8 weeks",
  "key_findings": [
    "85% retention improvement vs phonics-first",
    "Zero dropout rate across all participants",
    "100% self-reported comprehension"
  ],
  "theoretical": {
    "score": 0.82,
    "logical_consistency": 0.85,
    "conceptual_clarity": 0.80,
    "foundation_strength": 0.80,
    "breakthrough_potential": 0.83,
    "dependencies": ["Self-narrative theory", "Literacy research"]
  },
  "empirical": {
    "support_level": 0.91,
    "validation_type": "pilot",
    "reproducible": true,
    "evidence_sources": ["Field notes", "Pre/post assessments"]
  },
  "novelty": {
    "score": 0.78,
    "originality_score": 0.78,
    "paradigm_shift": false,
    "unique_contributions": ["Zero shame approach", "Self-story method"]
  },
  "impact": {
    "potential": 0.96,
    "academic_impact": 0.92,
    "industry_application": 0.95,
    "mission_alignment": 0.98
  },
  "synthesis": {
    "connections": ["b4e2c8a7", "c7d3a1f2"],
    "themes": ["Literacy liberation", "Shame elimination"],
    "contradictions": []
  },
  "routing_decision": "mission_critical",
  "priority_score": 0.96,
  "routing_explanation": "High mission alignment with strong empirical validation",
  "pictogram_hash": "L8E",
  "chrono_marker": "2024-12-06_VALIDATION_001",
  "vse_encoding": {
    "intent": "validation",
    "affect": 0.95,
    "certainty": 0.96,
    "context": ["literacy", "pilot", "field-test"]
  },
  "timestamp": "2024-12-06T14:30:45Z",
  "source": "field_study",
  "methodology": "8-week pilot with pre/post assessment, RCT design",
  "tags": ["literacy", "pilot", "field-test", "self-narrative"],
  "status": "validated"
}
```

---

## Database Format

### File Format

- **Format**: JSON
- **Extension**: `.json`
- **Encoding**: UTF-8
- **Structure**: Array of research packets

### Example Database

```json
[
  {
    "packet_id": "a3f7b921",
    "title": "First Research",
    ...
  },
  {
    "packet_id": "b4e2c8a7",
    "title": "Second Research",
    ...
  }
]
```

### Size Considerations

- **Small** (<100 packets): ~1 MB, instant loading
- **Medium** (100-1000 packets): ~10 MB, <1s loading
- **Large** (1000-10000 packets): ~100 MB, 1-5s loading
- **Very Large** (>10000 packets): Consider splitting databases

---

## Migration Guide

### From v1.0 to v1.5 (Planned)

```python
def migrate_v1_to_v1_5(packet_dict):
    """Migrate packet from v1.0 to v1.5 schema."""
    # Add new optional fields
    packet_dict.setdefault("embedding", None)
    packet_dict.setdefault("vector_id", None)
    packet_dict.setdefault("contradicts", [])
    packet_dict.setdefault("supports", [])
    packet_dict["schema_version"] = "1.5"
    return packet_dict
```

---

**Complete data model documentation. For usage examples, see [API.md](API.md) and [CLI_REFERENCE.md](CLI_REFERENCE.md).**
