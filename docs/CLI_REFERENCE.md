# ESPER-THESIS CLI Reference

Complete command-line interface documentation.

---

## Global Options

Available for all commands:

```bash
--database PATH      # Database location (default: ./research_db.json)
--project NAME       # Named project from config file
--version            # Show version and exit
--help               # Show help message
```

---

## Commands

### `create` - Create Research Packet

Create a new research packet with multi-agent analysis.

**Syntax:**
```bash
esper-thesis create \
  --title TEXT \
  --type {theory|validation|application|insight|synthesis|question|breakthrough} \
  --abstract TEXT \
  --findings TEXT [TEXT ...] \
  [OPTIONS]
```

**Required Arguments:**
- `--title` - Research title (string)
- `--type` - Research type (enum)
- `--abstract` - Brief description (string)
- `--findings` - Key findings (list of strings)

**Optional Arguments:**
- `--source TEXT` - Source type (default: "manual")
- `--methodology TEXT` - Research methodology description
- `--tags TAG [TAG ...]` - Tags for organization
- `--dry-run` - Preview without saving

**Examples:**
```bash
# Basic theory packet
esper-thesis create \
  --title "PICTOGRAM-256 Architecture" \
  --type theory \
  --abstract "Complete 256-glyph semantic system" \
  --findings "8-bit isomorphism" "Cryptographic binding"

# Validation with methodology
esper-thesis create \
  --title "Field Test Results" \
  --type validation \
  --abstract "50-learner pilot study" \
  --findings "85% improvement" "Zero dropout" \
  --methodology "Randomized controlled trial" \
  --tags pilot literacy field-test

# Dry run (preview)
esper-thesis create \
  --title "Test Research" \
  --type theory \
  --abstract "Testing packet creation" \
  --findings "Test finding" \
  --dry-run
```

**Output:**
```
✓ Created: a3f7b921
  Title: PICTOGRAM-256 Architecture
  Type: theory
  Routing: active_development
  Priority: 0.87
  Database: ./research_db.json
```

---

### `list` - Browse Research Packets

List and filter research packets.

**Syntax:**
```bash
esper-thesis list \
  [--type TYPE] \
  [--status STATUS] \
  [--sort {priority|date|novelty|impact}] \
  [--limit N]
```

**Optional Arguments:**
- `--type` - Filter by research type
- `--status` - Filter by status (draft/validated/published)
- `--sort` - Sort order (default: priority)
- `--limit` - Maximum packets to show (default: 20)

**Examples:**
```bash
# Top 10 by priority
esper-thesis list --sort priority --limit 10

# All validation research
esper-thesis list --type validation

# Published papers
esper-thesis list --status published

# Recent packets
esper-thesis list --sort date --limit 5
```

**Output:**
```
Research Packets (10 shown):

[b4e2c8a7] Self-Narrative Literacy Field Test
  Type: validation | Priority: 0.96

[a3f7b921] PICTOGRAM-256: Universal Semantic Communication
  Type: theory | Priority: 0.87

...
```

---

### `show` - Display Packet Details

Show complete information for a specific packet.

**Syntax:**
```bash
esper-thesis show PACKET_ID
```

**Arguments:**
- `PACKET_ID` - 8-character packet identifier

**Example:**
```bash
esper-thesis show a3f7b921
```

**Output:**
```
Research Packet: a3f7b921
==================================================

Title: PICTOGRAM-256: Universal Semantic Communication
Type: theory
Status: draft

Abstract:
Complete 256-glyph semantic system with cryptographic binding

Key Findings:
  • 8-bit isomorphism
  • Cryptographic binding

Multi-Agent Assessment:
  Theoretical: 0.87
    - Logical consistency: 0.90
    - Foundation strength: 0.85
    - Conceptual clarity: 0.88
    - Breakthrough potential: 0.85

  Empirical: 0.70
    - Support level: 0.70
    - Validation type: theoretical
    - Reproducible: false

  Novelty: 0.82
    - Originality score: 0.82
    - Paradigm shift: true

  Impact: 0.88
    - Academic impact: 0.85
    - Industry application: 0.80
    - Mission alignment: 0.95

  Synthesis: 0 connections

Routing: active_development
Priority: 0.87

ESPER-STACK Encoding:
  PICTOGRAM: T8A
  ChronoCore: 2024-12-06_143045
  VSE: intent=theory, certainty=0.87

Created: 2024-12-06 14:30:45
Database: ./research_db.json
```

---

### `stats` - Database Statistics

Show aggregate statistics for research database.

**Syntax:**
```bash
esper-thesis stats
```

**Example:**
```bash
esper-thesis stats
```

**Output:**
```
============================================================
ESPER-THESIS Statistics
============================================================

Total Packets: 47

By Type:
  validation     :  15
  theory         :  12
  application    :  10
  insight        :   8
  synthesis      :   2

By Routing:
  mission_critical   :   5
  active_development :  23
  synthesis_needed   :   8
  review_needed      :   3
  documentation      :   6
  archive            :   2

By Status:
  draft         :  35
  validated     :  10
  published     :   2

Average Priority: 0.74

Top 5 Priorities:
  1. [b4e2c8a7] Self-Narrative Literacy Field Test (0.96)
  2. [c7d3a1f2] Shame Elimination Mechanism (0.94)
  3. [a3f7b921] PICTOGRAM-256 Architecture (0.87)
  4. [e2f8b5c9] VSE Protocol Validation (0.85)
  5. [d4a7c3e1] ChronoCore Temporal Markers (0.83)
```

---

### `export` - Generate Reports

Export research packets in various formats.

**Syntax:**
```bash
esper-thesis export \
  [--format {json|markdown|summary}] \
  [--output FILE] \
  [--filter-type TYPE] \
  [--filter-status STATUS] \
  [--min-priority FLOAT]
```

**Optional Arguments:**
- `--format` - Output format (default: json)
- `--output` - Output file (default: stdout)
- `--filter-type` - Include only specific research type
- `--filter-status` - Include only specific status
- `--min-priority` - Minimum priority threshold (0.0-1.0)

**Examples:**
```bash
# Markdown report
esper-thesis export --format markdown --output findings.md

# High-priority JSON
esper-thesis export --format json --min-priority 0.8 --output high_priority.json

# Validation research only
esper-thesis export --format markdown --filter-type validation --output validations.md

# Published papers
esper-thesis export --format summary --filter-status published

# To stdout
esper-thesis export --format summary
```

**Markdown Output Example:**
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

**Assessment**:
- Theoretical: 0.82
- Empirical: 0.91
- Novelty: 0.78
- Impact: 0.96

---
```

---

### `update` - Modify Packet Status

Update research packet status.

**Syntax:**
```bash
esper-thesis update PACKET_ID --status {draft|validated|published}
```

**Arguments:**
- `PACKET_ID` - 8-character packet identifier
- `--status` - New status value

**Examples:**
```bash
# Mark as validated
esper-thesis update a3f7b921 --status validated

# Mark as published
esper-thesis update b4e2c8a7 --status published
```

**Output:**
```
✓ Updated: a3f7b921
  Status: draft → validated
```

---

### `config` - Configuration Management

Manage ESPER-THESIS configuration.

**Syntax:**
```bash
esper-thesis config {init|show|schema}
```

**Subcommands:**

#### `config init`
Create configuration template.

```bash
esper-thesis config init
```

**Output:**
```
Created config template: /home/user/.esper_thesis/config.json

Edit this file to configure:
  - default_database: Global research database path
  - projects: Named project-specific databases
```

#### `config show`
Display current configuration and resolution behavior.

```bash
esper-thesis config show
```

**Output:**
```
============================================================
ESPER-THESIS Configuration
============================================================

Database Resolution Order:
  1. CLI argument:    --database <path>
  2. Environment var: ESPER_THESIS_DB
  3. Config file:     /home/user/.esper_thesis/config.json
  4. Default:         research_db.json

Current Environment:
  ESPER_THESIS_DB = (not set)

Config File:
  Location: /home/user/.esper_thesis/config.json
  Status:   Exists
  Default:  ~/research/global.json
  Projects: 3 configured
    - literacy: ~/projects/literacy/research.json
    - nasa: ~/projects/nasa/research.json
    - esper-stack: ~/esper/research.json

Current Resolution:
  Database: /home/user/research/global.json
  Absolute: /home/user/research/global.json
  Exists:   true
```

#### `config schema`
Display research packet schema.

```bash
esper-thesis config schema
```

**Output:**
```
Research Packet Schema v1.0
============================================================

Required Fields:
  --title       : Research title (string)
  --type        : Research type (enum)
  --abstract    : Brief description (string)
  --findings    : Key findings (list of strings)

Optional Fields:
  --source      : Source type (default: 'manual')
  --methodology : Research methodology (string)
  --tags        : Tags for organization (list)

Research Types:
  theory         : Conceptual frameworks, models
  validation     : Empirical tests, experiments
  application    : Real-world implementations
  insight        : Observations, connections
  synthesis      : Integration across findings
  question       : Open research inquiries
  breakthrough   : Paradigm-shifting discoveries

Routing Decisions:
  mission_critical   : Direct literacy impact (priority 0.95-1.0)
  active_development : High potential, needs work (0.80-0.90)
  synthesis_needed   : Multiple connections (0.70-0.80)
  review_needed      : Issues to address (0.85-0.95)
  documentation      : Ready for publication (0.65-0.75)
  archive            : Complete, integrated (0.20-0.40)
```

---

## Exit Codes

- `0` - Success
- `1` - General error (invalid input, processing failure)
- `2` - Invalid arguments (wrong command, missing required args)
- `3` - Database error (file not found, corrupt JSON, write failure)
- `4` - Not found (packet ID doesn't exist, project not in config)

**Example:**
```bash
esper-thesis show invalid-id
echo $?
# Output: 4
```

---

## Environment Variables

### `ESPER_THESIS_DB`

Set default database location for all commands.

```bash
export ESPER_THESIS_DB=~/research/main.json
esper-thesis create ...  # Uses ~/research/main.json
```

**Priority**: CLI `--database` argument overrides this.

---

## Configuration File

### Location

`~/.esper_thesis/config.json`

### Format

```json
{
  "default_database": "~/research/global.json",
  "projects": {
    "literacy": "~/projects/literacy/research.json",
    "nasa": "~/projects/nasa/research.json",
    "esper-stack": "~/esper/research.json"
  }
}
```

### Fields

- `default_database` - Global database path (optional, uses local if null)
- `projects` - Named project databases (optional)

### Usage

```bash
# Create in specific project
esper-thesis --project literacy create ...

# List projects in config
esper-thesis config show
```

---

## Shell Completion

### Bash

```bash
# Add to ~/.bashrc
eval "$(_ESPER_THESIS_COMPLETE=bash_source esper-thesis)"
```

### Zsh

```bash
# Add to ~/.zshrc
eval "$(_ESPER_THESIS_COMPLETE=zsh_source esper-thesis)"
```

---

## Tips & Best Practices

### Efficient Workflows

```bash
# Quick check what's high priority
alias et-top='esper-thesis list --sort priority --limit 5'

# Export today's work
alias et-today='esper-thesis export --format markdown --output today.md'

# Stats at a glance
alias et-stats='esper-thesis stats'
```

### Database Management

```bash
# Backup database
cp research_db.json research_db.backup.json

# Merge databases
cat db1.json db2.json | jq -s 'add' > merged.json

# View as JSON
cat research_db.json | jq '.'
```

### Batch Operations

```bash
# Create multiple packets from CSV
while IFS=, read -r title type abstract findings; do
    esper-thesis create \
        --title "$title" \
        --type "$type" \
        --abstract "$abstract" \
        --findings "$findings"
done < research.csv
```

---

## Troubleshooting

### Command not found

```bash
which esper-thesis
# If empty, reinstall:
pip install --force-reinstall esper-thesis
```

### Database permission denied

```bash
# Check permissions
ls -l research_db.json

# Fix permissions
chmod 644 research_db.json
```

### Corrupt database

```bash
# Validate JSON
python -m json.tool research_db.json

# Restore from backup
cp research_db.backup.json research_db.json
```

---

**Complete CLI documentation. For library usage, see [API.md](API.md).**
