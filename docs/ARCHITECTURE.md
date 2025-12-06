# ESPER-THESIS Architecture

Complete system design and integration documentation.

---

## System Overview

ESPER-THESIS is a semantic intelligence system that transforms unstructured research into analyzed, prioritized knowledge packets through a 5-agent analysis pipeline.

**Core Philosophy**: Transparent, auditable semantic AI serving literacy liberation.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Interface                           │
│  ┌──────────────────────┐  ┌──────────────────────────────┐   │
│  │   CLI (argparse)     │  │   Python API (library)       │   │
│  │   esper-thesis       │  │   process_research_item()    │   │
│  └──────────┬───────────┘  └──────────┬───────────────────┘   │
└─────────────┼──────────────────────────┼───────────────────────┘
              │                          │
              └──────────┬───────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Research Processor                           │
│  • Parse & validate input                                       │
│  • Generate packet_id (PSH-256)                                 │
│  • Create timestamp (ISO 8601)                                  │
│  • Initialize ResearchPacket                                    │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              5-Agent Analysis Pipeline (Parallel)               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐           │
│  │ Theoretical  │ │  Empirical   │ │   Novelty    │           │
│  │    Agent     │ │    Agent     │ │    Agent     │           │
│  │              │ │              │ │              │           │
│  │ • Logic      │ │ • Validation │ │ • Origin-    │           │
│  │ • Clarity    │ │ • Evidence   │ │   ality      │           │
│  │ • Foundation │ │ • Repro-     │ │ • Paradigm   │           │
│  │ • Break-     │ │   ducibility │ │   shift      │           │
│  │   through    │ │              │ │              │           │
│  └──────────────┘ └──────────────┘ └──────────────┘           │
│  ┌──────────────┐ ┌──────────────┐                            │
│  │   Impact     │ │  Synthesis   │                            │
│  │    Agent     │ │    Agent     │                            │
│  │              │ │              │                            │
│  │ • Academic   │ │ • Connections│                            │
│  │ • Industry   │ │ • Themes     │                            │
│  │ • Mission    │ │ • Contra-    │                            │
│  │              │ │   dictions   │                            │
│  └──────────────┘ └──────────────┘                            │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              ESPER-STACK Semantic Encoding                      │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐  │
│  │ PICTOGRAM-256   │ │   ChronoCore    │ │  VSE Protocol   │  │
│  │                 │ │                 │ │                 │  │
│  │ • PSH-256 hash  │ │ • Temporal      │ │ • Intent        │  │
│  │ • 3-char glyph  │ │   markers       │ │ • Affect        │  │
│  │ • Semantic      │ │ • Daily         │ │ • Certainty     │  │
│  │   binding       │ │   sequence      │ │ • Context       │  │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘  │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Intelligent Router (6 Decisions)                   │
│  • Calculate weighted priority score                            │
│  • Determine routing decision                                   │
│  • Generate human-readable explanation                          │
│  • Apply bonuses (paradigm shift, connections, etc.)            │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│             Storage Layer (Configurable)                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  4-Level Database Resolution Cascade                     │  │
│  │  1. CLI argument (--database)                            │  │
│  │  2. Environment variable (ESPER_THESIS_DB)               │  │
│  │  3. Config file (~/.esper_thesis/config.json)            │  │
│  │  4. Default (./research_db.json)                         │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  • JSON format (UTF-8)                                          │
│  • Array of ResearchPackets                                    │
│  • Atomic writes (temp + rename)                               │
│  • Backup on modification                                      │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Export & Query Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │     JSON     │  │   Markdown   │  │   Summary    │         │
│  │              │  │              │  │              │         │
│  │ • APIs       │  │ • Docs       │  │ • Human      │         │
│  │ • Databases  │  │ • Papers     │  │   readable   │         │
│  │ • Machine    │  │ • Reports    │  │ • Quick      │         │
│  │   readable   │  │              │  │   view       │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
│  • Filtering (type, status, priority)                          │
│  • Sorting (priority, date, novelty, impact)                   │
│  • Pagination (limit)                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Architecture

### 1. Research Processor (`processor.py`)

**Responsibilities**:
- Input validation
- Packet ID generation
- Timestamp creation
- Agent orchestration
- ESPER-STACK encoding
- Routing coordination

**Key Function**:
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

**Flow**:
1. Validate inputs (length, format)
2. Generate packet_id via PSH-256
3. Create ISO 8601 timestamp
4. Run 5 agents in parallel
5. Apply ESPER-STACK encoding
6. Calculate routing + priority
7. Return complete ResearchPacket

### 2. Five-Agent System (`agents.py`)

#### Theoretical Agent
**Purpose**: Assess conceptual coherence and breakthrough potential

**Inputs**: title, abstract, key_findings, methodology

**Outputs**:
- `score` (0.0-1.0)
- `logical_consistency`
- `conceptual_clarity`
- `foundation_strength`
- `breakthrough_potential`
- `dependencies` (list)

**Algorithm**:
```python
# Assess logical structure
logical = analyze_logical_flow(title, abstract, findings)

# Evaluate clarity
clarity = measure_clarity(abstract, findings)

# Check foundations
foundation = detect_prior_work(abstract, methodology)

# Detect breakthroughs
breakthrough = detect_breakthrough_keywords(title, abstract)

# Compute weighted average
score = (logical + clarity + foundation + breakthrough) / 4
```

#### Empirical Agent
**Purpose**: Track validation evidence and reproducibility

**Inputs**: title, abstract, key_findings, methodology, research_type

**Outputs**:
- `support_level` (0.0-1.0)
- `validation_type` (enum)
- `reproducible` (bool)
- `evidence_sources` (list)

**Validation Type Mapping**:
- `VALIDATION` research → "validated" or "pilot"
- `APPLICATION` research → "preliminary"
- `THEORY` research → "theoretical"
- Others → "preliminary"

#### Novelty Agent
**Purpose**: Evaluate originality and paradigm shift potential

**Inputs**: title, abstract, key_findings, research_type

**Outputs**:
- `score` (0.0-1.0)
- `originality_score`
- `paradigm_shift` (bool)
- `unique_contributions` (list)

**Paradigm Shift Detection**:
```python
breakthrough_keywords = [
    "first", "never", "paradigm", "revolutionary",
    "breakthrough", "novel", "unique", "unprecedented"
]

paradigm_shift = (
    research_type == BREAKTHROUGH or
    any(kw in title.lower() for kw in breakthrough_keywords) or
    len(unique_contributions) >= 3
)
```

#### Impact Agent
**Purpose**: Measure significance and mission alignment

**Inputs**: title, abstract, key_findings, research_type

**Outputs**:
- `potential` (0.0-1.0)
- `academic_impact`
- `industry_application`
- `mission_alignment`

**Mission Alignment Scoring**:
```python
literacy_keywords = {
    "high": ["literacy", "reading", "learner", "shame"],
    "medium": ["teaching", "learning", "comprehension"],
    "low": []  # Everything else
}

mission_score = calculate_keyword_density(
    text=title + abstract + " ".join(findings),
    keywords=literacy_keywords
)
```

#### Synthesis Agent
**Purpose**: Discover connections to other research

**Inputs**: packet, existing_packets (database)

**Outputs**:
- `connections` (list of packet IDs)
- `themes` (list of strings)
- `contradictions` (list of packet IDs)

**Connection Algorithm**:
```python
# Extract keywords
keywords = extract_keywords(packet)

# Find overlapping packets
connections = []
for other in existing_packets:
    other_keywords = extract_keywords(other)
    overlap = len(keywords & other_keywords)
    if overlap >= 2:
        connections.append(other.packet_id)

# Detect themes
themes = cluster_keywords(all_connected_keywords)

# Find contradictions (future v1.5)
contradictions = detect_opposing_claims(packet, connections)
```

### 3. Intelligent Router (`router.py`)

**Responsibilities**:
- Calculate priority score
- Determine routing decision
- Generate explanation

**Priority Calculation**:
```python
priority = (
    theoretical.score * 0.20 +
    empirical.support_level * 0.20 +
    novelty.score * 0.20 +
    impact.potential * 0.30 +
    impact.mission_alignment * 0.10
)

# Apply bonuses
if novelty.paradigm_shift:
    priority += 0.05
if research_type == BREAKTHROUGH:
    priority += 0.10
if len(synthesis.connections) >= 5:
    priority += 0.05

# Clamp to [0, 1]
priority = min(1.0, max(0.0, priority))
```

**Routing Decision Logic**:
```python
if priority >= 0.95 and mission_alignment > 0.8:
    return MISSION_CRITICAL
elif priority >= 0.85 and empirical.support_level < 0.6:
    return REVIEW_NEEDED
elif len(synthesis.connections) >= 3:
    return SYNTHESIS_NEEDED
elif priority >= 0.80:
    return ACTIVE_DEVELOPMENT
elif status == "published":
    return ARCHIVE
else:
    return DOCUMENTATION
```

### 4. ESPER-STACK Integration (`router.py`)

#### PICTOGRAM-256 Encoding
```python
def generate_pictogram_hash(title: str) -> str:
    """Generate 3-character semantic glyph."""
    # PSH-256 hash
    hash_bytes = hashlib.sha256(title.encode('utf-8')).digest()
    
    # Map to PICTOGRAM-256 space (0-255)
    indices = [hash_bytes[i] for i in range(3)]
    
    # Convert to base-85 glyphs
    glyphs = [PICTOGRAM_ALPHABET[idx % 85] for idx in indices]
    
    return ''.join(glyphs)  # e.g., "T8A"
```

#### ChronoCore Markers
```python
def generate_chrono_marker(
    timestamp: str,
    research_type: ResearchType
) -> str:
    """Generate temporal marker."""
    date = timestamp.split('T')[0]  # "2024-12-06"
    type_str = research_type.value.upper()
    sequence = get_daily_sequence(date, research_type)
    
    return f"{date}_{type_str}_{sequence:03d}"
    # e.g., "2024-12-06_THEORY_001"
```

#### VSE Protocol
```python
def encode_vse(packet: ResearchPacket) -> Dict[str, Any]:
    """Encode VSE Protocol."""
    return {
        "intent": packet.research_type.value,
        "affect": calculate_affect(packet),  # Emotional valence
        "certainty": packet.priority_score,
        "context": packet.tags
    }
```

### 5. Storage Layer (`storage.py`)

**Database Operations**:

```python
def load_database(db_path: str) -> List[ResearchPacket]:
    """Load packets from JSON."""
    with open(db_path, 'r') as f:
        data = json.load(f)
    return [ResearchPacket.from_dict(p) for p in data]

def save_database(
    packets: List[ResearchPacket],
    db_path: str
) -> None:
    """Save packets with atomic write."""
    # Write to temp file
    temp_path = db_path + '.tmp'
    with open(temp_path, 'w') as f:
        json.dump([p.to_dict() for p in packets], f, indent=2)
    
    # Atomic rename
    os.replace(temp_path, db_path)
```

**Configuration Resolution**:
```python
def get_database_path(
    cli_path: Optional[str] = None,
    project: Optional[str] = None
) -> str:
    """4-level cascade resolution."""
    # 1. CLI argument
    if cli_path:
        return os.path.expanduser(cli_path)
    
    # 2. Environment variable
    if "ESPER_THESIS_DB" in os.environ:
        return os.path.expanduser(os.environ["ESPER_THESIS_DB"])
    
    # 3. Config file
    config = load_config()
    if project and project in config.get("projects", {}):
        return os.path.expanduser(config["projects"][project])
    if "default_database" in config:
        return os.path.expanduser(config["default_database"])
    
    # 4. Default
    return "./research_db.json"
```

---

## ESPER-STACK Integration

### Complete Ecosystem

```
┌──────────────────────────────────────────────────────────────┐
│                      ESPER-STACK                             │
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │ ESPER-Email     │  │ ESPER-THESIS    │  │   Future    │ │
│  │ Swarm           │  │                 │  │  Components │ │
│  │                 │  │                 │  │             │ │
│  │ (Email          │  │ (Research       │  │ (TBD)       │ │
│  │  management)    │  │  management)    │  │             │ │
│  └────────┬────────┘  └────────┬────────┘  └─────────────┘ │
│           │                    │                            │
│           └────────┬───────────┘                            │
│                    │                                        │
│         ┌──────────▼────────────┐                          │
│         │  Shared Substrate:    │                          │
│         │  • PICTOGRAM-256      │                          │
│         │  • ChronoCore         │                          │
│         │  • VSE Protocol       │                          │
│         └───────────────────────┘                          │
└──────────────────────────────────────────────────────────────┘
```

### Semantic Interoperability

**PICTOGRAM-256**:
- Universal 256-glyph semantic system
- Each glyph = 1 byte = 1 semantic atom
- PSH-256 cryptographic binding
- Geometric universals (topology-based)

**ChronoCore**:
- Temporal mechanics substrate
- Enables time-based reasoning
- Supports causality tracking
- Foundation for higher concepts

**VSE Protocol**:
- Volume-Semantic-Encoding
- Compact semantic representation
- Intent, affect, certainty, context
- Enables cross-system understanding

---

## Data Flow

### Packet Creation Flow

```
User Input
    ↓
Validation
    ↓
Packet ID Generation (PSH-256)
    ↓
Timestamp Creation (ISO 8601)
    ↓
┌─────────────────────────────────┐
│  5-Agent Parallel Analysis      │
│  ┌─────────┐ ┌─────────┐       │
│  │Theoret. │ │Empirical│       │
│  └────┬────┘ └────┬────┘       │
│       │           │             │
│  ┌────┴────┐ ┌───┴─────┐       │
│  │ Novelty │ │ Impact  │       │
│  └────┬────┘ └────┬────┘       │
│       │           │             │
│       └─────┬─────┘             │
│             │                   │
│        ┌────┴────┐              │
│        │Synthesis│              │
│        └─────────┘              │
└─────────────┬───────────────────┘
              ↓
ESPER-STACK Encoding
    ↓
Routing Calculation
    ↓
ResearchPacket (Complete)
    ↓
Storage (JSON)
```

### Query Flow

```
User Query (CLI/API)
    ↓
Database Path Resolution (4-level)
    ↓
Load Database (JSON → ResearchPacket[])
    ↓
Filter (type, status, priority)
    ↓
Sort (priority, date, novelty, impact)
    ↓
Limit (pagination)
    ↓
Format (JSON, Markdown, Summary)
    ↓
Return to User
```

---

## Design Patterns

### 1. Dependency Injection
All agents receive data via parameters, no global state.

```python
# Good: Pure function
def theoretical_agent(title, abstract, findings, methodology):
    return TheoreticalAssessment(...)

# Bad: Global state
# theoretical_agent() reads from global CURRENT_PACKET
```

### 2. Immutability
ResearchPackets are immutable after creation (except status updates).

```python
# Packets are frozen dataclasses
@dataclass(frozen=True)
class ResearchPacket:
    packet_id: str
    # ...
```

### 3. Deterministic Processing
Same inputs always produce same outputs (no randomness).

```python
# Priority calculation is pure function
priority = calculate_priority(theoretical, empirical, novelty, impact)
# No random.random(), no time.time() in calculations
```

### 4. Fail-Fast Validation
Input validation happens immediately at entry points.

```python
def process_research_item(title, ...):
    if not title or len(title) > 200:
        raise ValueError("Title must be 1-200 characters")
    # Continue processing...
```

### 5. Atomic Writes
Database writes use temp file + atomic rename.

```python
# Write to temp
with open(db_path + '.tmp', 'w') as f:
    json.dump(data, f)

# Atomic rename (POSIX guarantee)
os.replace(db_path + '.tmp', db_path)
```

---

## Performance Characteristics

### Time Complexity

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| Create packet | O(n) | n = existing packets (for synthesis) |
| Load database | O(m) | m = total packets |
| List packets | O(m log m) | Sort dominates |
| Export | O(m) | Filter + format |
| Update status | O(m) | Load + modify + save |

### Space Complexity

| Component | Memory | Disk |
|-----------|--------|------|
| ResearchPacket | ~2 KB | ~3 KB (JSON) |
| 100 packets | ~200 KB | ~300 KB |
| 1000 packets | ~2 MB | ~3 MB |
| 10000 packets | ~20 MB | ~30 MB |

### Scalability Limits

**Current (v1.0)**:
- **Packets**: Up to ~10,000 efficient
- **Synthesis**: O(n²) keyword matching
- **Database**: Single JSON file
- **Concurrency**: None (single-user)

**Future (v1.5)**:
- **Packets**: 100,000+ with vector store
- **Synthesis**: O(log n) with embeddings
- **Database**: Optional SQLite backend
- **Concurrency**: File locking

---

## Extension Points

### Custom Agents

```python
from esper_thesis.agents import BaseAgent

class CustomAgent(BaseAgent):
    """Custom analysis agent."""
    
    def analyze(self, packet: ResearchPacket) -> CustomAssessment:
        # Your logic here
        return CustomAssessment(...)

# Register agent
register_agent("custom", CustomAgent())
```

### Custom Routing

```python
from esper_thesis.router import BaseRouter

class CustomRouter(BaseRouter):
    """Custom routing logic."""
    
    def route(self, packet: ResearchPacket) -> Tuple[RoutingDecision, float, str]:
        # Your logic here
        return decision, priority, explanation

# Use custom router
set_router(CustomRouter())
```

### Storage Backends

```python
from esper_thesis.storage import BaseStorage

class SQLiteStorage(BaseStorage):
    """SQLite storage backend."""
    
    def load(self, path: str) -> List[ResearchPacket]:
        # SQL query
        pass
    
    def save(self, packets: List[ResearchPacket], path: str):
        # SQL insert/update
        pass

# Use custom storage
set_storage(SQLiteStorage())
```

---

## Security Considerations

### Input Validation
- All user inputs sanitized
- Length limits enforced
- Type checking via Python type hints

### File System
- No arbitrary path execution
- Path expansion controlled
- Atomic writes prevent corruption

### Data Integrity
- PSH-256 cryptographic binding
- JSON schema validation
- Immutable packets (frozen dataclasses)

### Privacy
- All data local by default
- No external API calls
- User controls all storage

---

## Future Architecture (v2.0)

### Swarm Intelligence Integration

```
┌─────────────────────────────────────────────────────────────┐
│                   Swarm Coordinator (Grok)                  │
└─────────────┬───────────────────────────────┬───────────────┘
              │                               │
    ┌─────────▼─────────┐         ┌─────────▼─────────┐
    │  Seeker Agents    │         │  Critic Agents    │
    │  (8-32 parallel)  │         │  (Validation)     │
    └─────────┬─────────┘         └─────────┬─────────┘
              │                               │
              └───────────┬───────────────────┘
                          │
              ┌───────────▼───────────┐
              │  ESPER-THESIS v1.0    │
              │  (Assessment Layer)   │
              └───────────┬───────────┘
                          │
              ┌───────────▼───────────┐
              │  Living Thesis        │
              │  Renderer             │
              └───────────────────────┘
```

See [SWARM_VISION.md](SWARM_VISION.md) for complete v2.0 architecture.

---

**Complete architecture documentation. For implementation details, see [API.md](API.md) and source code.**
