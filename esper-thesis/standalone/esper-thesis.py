#!/usr/bin/env python3
"""
ESPER-THESIS: Research Management & Academic Organization System
Single-file standalone version

A 5-agent semantic intelligence system for organizing research findings.

Usage:
    python esper-thesis.py create --title "Research Title" --type theory \\
        --abstract "Abstract text" --findings "Finding 1" "Finding 2"
    
    python esper-thesis.py ingest --conversation transcript.txt --id conv-001
    
    python esper-thesis.py export --format markdown --output findings.md
    
    python esper-thesis.py list --sort priority
    
    python esper-thesis.py stats

Mission: Supporting literacy liberation through rigorous academic research.
"""

import argparse
import json
import re
import sys
import uuid
import hashlib
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Dict, Optional, Tuple

__version__ = "1.0.0"


# ============================================================================
# DATA MODELS
# ============================================================================

class ResearchType(Enum):
    """Categories of research contributions."""
    THEORY = "theory"
    VALIDATION = "validation"
    APPLICATION = "application"
    INSIGHT = "insight"
    SYNTHESIS = "synthesis"
    QUESTION = "question"
    BREAKTHROUGH = "breakthrough"


class RoutingDecision(Enum):
    """Research packet routing destinations."""
    ACTIVE_DEVELOPMENT = "active_development"
    SYNTHESIS_NEEDED = "synthesis_needed"
    REVIEW_NEEDED = "review_needed"
    DOCUMENTATION = "documentation"
    ARCHIVE = "archive"
    MISSION_CRITICAL = "mission_critical"


@dataclass
class TheoreticalAssessment:
    """Theoretical coherence evaluation."""
    score: float
    logical_consistency: float
    foundation_strength: float
    conceptual_clarity: float
    breakthrough_potential: float
    dependencies: List[str]
    issues: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class EmpiricalEvidence:
    """Empirical validation tracking."""
    support_level: float
    validation_type: str
    validating_system: str
    timestamp: datetime
    description: str
    reproducible: bool
    data_location: Optional[str] = None
    contradictions: List[str] = field(default_factory=list)


@dataclass
class NoveltyRating:
    """Originality and innovation assessment."""
    score: float
    comparison_to_prior_art: str
    unique_contributions: List[str]
    paradigm_shift: bool
    lineage: List[str]
    notes: str = ""


@dataclass
class ImpactAnalysis:
    """Significance and reach evaluation."""
    potential: float
    academic_impact: float
    industry_application: float
    mission_alignment: float
    cross_domain_reach: List[str]
    timeline_to_impact: str
    notes: str = ""


@dataclass
class SynthesisConnection:
    """Links between research packets."""
    related_packet_id: str
    connection_type: str
    strength: float
    description: str


@dataclass
class ResearchPacket:
    """A semantic packet representing research finding."""
    packet_id: str
    title: str
    research_type: ResearchType
    timestamp: datetime
    source: str
    source_location: Optional[str] = None
    
    pictogram_hash: str = ""
    vse_encoding: Dict = field(default_factory=dict)
    chrono_marker: str = ""
    
    theoretical: Optional[TheoreticalAssessment] = None
    empirical: List[EmpiricalEvidence] = field(default_factory=list)
    novelty: Optional[NoveltyRating] = None
    impact: Optional[ImpactAnalysis] = None
    synthesis: List[SynthesisConnection] = field(default_factory=list)
    
    abstract: str = ""
    key_findings: List[str] = field(default_factory=list)
    methodology: str = ""
    open_questions: List[str] = field(default_factory=list)
    
    routing_decision: Optional[RoutingDecision] = None
    priority_score: float = 0.0
    
    tags: List[str] = field(default_factory=list)
    collaborators: List[str] = field(default_factory=list)
    status: str = "draft"


# ============================================================================
# AGENTS
# ============================================================================

def theoretical_agent(title: str, abstract: str, key_findings: List[str], 
                     methodology: str) -> TheoreticalAssessment:
    """Evaluate theoretical coherence and conceptual soundness."""
    
    logic_score = 0.8
    if "because" in abstract.lower() or "therefore" in abstract.lower():
        logic_score += 0.1
    if "however" in abstract.lower() or "although" in abstract.lower():
        logic_score += 0.05
    logic_score = min(1.0, logic_score)
    
    foundation_keywords = ["builds on", "extends", "based on", "following", "prior"]
    foundation_score = 0.5
    for keyword in foundation_keywords:
        if keyword in abstract.lower():
            foundation_score += 0.1
    foundation_score = min(1.0, foundation_score)
    
    clarity_score = 0.7
    if len(abstract.split('.')) >= 3:
        clarity_score += 0.1
    if len(key_findings) >= 2:
        clarity_score += 0.1
    clarity_score = min(1.0, clarity_score)
    
    breakthrough_keywords = [
        "first", "novel", "unprecedented", "breakthrough", "revolutionary",
        "paradigm", "fundamental", "groundbreaking", "transforms"
    ]
    breakthrough_score = 0.3
    text = (title + " " + abstract).lower()
    for keyword in breakthrough_keywords:
        if keyword in text:
            breakthrough_score += 0.15
    breakthrough_score = min(1.0, breakthrough_score)
    
    dependencies = []
    dep_patterns = [r"requires (\w+)", r"depends on (\w+)", r"assumes (\w+)"]
    for pattern in dep_patterns:
        matches = re.findall(pattern, abstract.lower())
        dependencies.extend(matches)
    
    issues = []
    if "contradiction" in abstract.lower():
        issues.append("Potential internal contradiction detected")
    if "unclear" in abstract.lower() or "ambiguous" in abstract.lower():
        issues.append("Conceptual ambiguity noted")
    
    theoretical_score = (
        logic_score * 0.3 +
        foundation_score * 0.2 +
        clarity_score * 0.2 +
        breakthrough_score * 0.3
    )
    
    return TheoreticalAssessment(
        score=theoretical_score,
        logical_consistency=logic_score,
        foundation_strength=foundation_score,
        conceptual_clarity=clarity_score,
        breakthrough_potential=breakthrough_score,
        dependencies=list(set(dependencies)),
        issues=issues,
        notes=f"Evaluated {len(key_findings)} key findings"
    )


def empirical_agent(title: str, abstract: str, methodology: str, 
                   source: str) -> EmpiricalEvidence:
    """Assess empirical validation and evidence strength."""
    
    validation_type = "theoretical"
    if "validated by" in abstract.lower() or "tested with" in abstract.lower():
        validation_type = "experiment"
    if any(s in abstract.lower() for s in ["claude", "gpt", "perplexity", "ai system"]):
        validation_type = "ai_system"
    if "field test" in abstract.lower() or "real-world" in abstract.lower():
        validation_type = "field_test"
    
    validating_system = "pending"
    ai_systems = ["claude", "perplexity", "vox", "gemini", "grok", "copilot"]
    for system in ai_systems:
        if system in (title + " " + abstract).lower():
            validating_system = system.title()
            break
    
    if "turing tour" in abstract.lower():
        validating_system = "Turing Tour (5 AI systems)"
    
    support_level = 0.5
    if validation_type == "ai_system":
        support_level = 0.7
    elif validation_type == "experiment":
        support_level = 0.8
    elif validation_type == "field_test":
        support_level = 0.9
    
    reproducible = "reproducible" in abstract.lower() or "replicated" in abstract.lower()
    
    contradictions = []
    if "inconsistent" in abstract.lower():
        contradictions.append("Inconsistency noted in abstract")
    
    description = f"{validation_type.replace('_', ' ').title()} validation"
    if validating_system != "pending":
        description += f" by {validating_system}"
    
    return EmpiricalEvidence(
        support_level=support_level,
        validation_type=validation_type,
        validating_system=validating_system,
        timestamp=datetime.now(),
        description=description,
        reproducible=reproducible,
        contradictions=contradictions
    )


def novelty_agent(title: str, abstract: str, key_findings: List[str],
                 existing_packets: List[Dict]) -> NoveltyRating:
    """Evaluate originality and innovation."""
    
    novelty_keywords = [
        "first", "novel", "new", "innovative", "original", "unprecedented",
        "unique", "groundbreaking", "pioneering"
    ]
    text = (title + " " + abstract).lower()
    novelty_score = 0.5
    for keyword in novelty_keywords:
        if keyword in text:
            novelty_score += 0.1
    novelty_score = min(1.0, novelty_score)
    
    paradigm_indicators = [
        "paradigm", "revolutionary", "transforms", "fundamentally changes",
        "redefines", "breakthrough"
    ]
    paradigm_shift = any(indicator in text for indicator in paradigm_indicators)
    
    similar_packets = []
    for packet in existing_packets:
        if any(word in packet.get('title', '').lower() for word in title.lower().split()):
            similar_packets.append(packet['packet_id'])
    
    if len(similar_packets) > 3:
        novelty_score *= 0.8
    
    unique_contributions = []
    for finding in key_findings:
        if any(marker in finding.lower() for marker in ["first", "only", "unique", "novel"]):
            unique_contributions.append(finding)
    
    if not unique_contributions:
        unique_contributions = key_findings[:2]
    
    comparison = "This work"
    if similar_packets:
        comparison += f" builds on {len(similar_packets)} related findings"
    else:
        comparison += " appears to open new research territory"
    
    if paradigm_shift:
        comparison += " and represents a paradigm shift"
    
    return NoveltyRating(
        score=novelty_score,
        comparison_to_prior_art=comparison,
        unique_contributions=unique_contributions,
        paradigm_shift=paradigm_shift,
        lineage=similar_packets[:5],
        notes=f"Compared against {len(existing_packets)} existing packets"
    )


def impact_agent(title: str, abstract: str, research_type: str,
                key_findings: List[str]) -> ImpactAnalysis:
    """Measure significance and potential reach."""
    
    text = (title + " " + abstract).lower()
    
    academic_keywords = [
        "theory", "framework", "model", "hypothesis", "validation",
        "empirical", "research", "study"
    ]
    academic_score = 0.5
    for keyword in academic_keywords:
        if keyword in text:
            academic_score += 0.08
    academic_score = min(1.0, academic_score)
    
    industry_keywords = [
        "application", "implementation", "production", "commercial",
        "practical", "real-world", "deployment"
    ]
    industry_score = 0.4
    for keyword in industry_keywords:
        if keyword in text:
            industry_score += 0.1
    industry_score = min(1.0, industry_score)
    
    mission_keywords = [
        "literacy", "reading", "teaching", "education", "learning",
        "accessible", "narrative", "comprehension", "liberation"
    ]
    mission_score = 0.3
    for keyword in mission_keywords:
        if keyword in text:
            mission_score += 0.15
    mission_score = min(1.0, mission_score)
    
    domains = []
    domain_map = {
        "ai": ["artificial intelligence", "machine learning", "ai"],
        "linguistics": ["language", "semantic", "linguistic"],
        "education": ["teaching", "learning", "education"],
        "psychology": ["cognitive", "psychology", "emotion"],
        "computer_science": ["algorithm", "computation", "software"]
    }
    
    for domain, keywords in domain_map.items():
        if any(keyword in text for keyword in keywords):
            domains.append(domain)
    
    timeline = "near_term"
    if "immediate" in text or "now" in text:
        timeline = "immediate"
    elif "future" in text or "long-term" in text:
        timeline = "long_term"
    
    impact_potential = (
        academic_score * 0.25 +
        industry_score * 0.25 +
        mission_score * 0.4 +
        (len(domains) / 5) * 0.1
    )
    
    notes = []
    if mission_score > 0.7:
        notes.append("Strong mission alignment - direct literacy impact")
    if len(domains) >= 3:
        notes.append(f"Cross-domain reach: {', '.join(domains)}")
    
    return ImpactAnalysis(
        potential=impact_potential,
        academic_impact=academic_score,
        industry_application=industry_score,
        mission_alignment=mission_score,
        cross_domain_reach=domains,
        timeline_to_impact=timeline,
        notes=" | ".join(notes) if notes else ""
    )


def synthesis_agent(packet_id: str, title: str, abstract: str,
                   key_findings: List[str], existing_packets: List[Dict]) -> List[SynthesisConnection]:
    """Discover connections between research packets."""
    
    connections = []
    
    my_keywords = set(
        word.lower() for word in (title + " " + abstract).split()
        if len(word) > 4 and word.isalnum()
    )
    
    for other_packet in existing_packets:
        if other_packet['packet_id'] == packet_id:
            continue
        
        other_text = other_packet.get('title', '') + " " + other_packet.get('abstract', '')
        other_keywords = set(
            word.lower() for word in other_text.split()
            if len(word) > 4 and word.isalnum()
        )
        
        overlap = my_keywords & other_keywords
        if len(overlap) < 2:
            continue
        
        strength = min(1.0, len(overlap) / 10)
        
        connection_type = "related"
        if "builds on" in abstract.lower():
            connection_type = "builds_on"
        elif "validates" in abstract.lower():
            connection_type = "validates"
        elif "extends" in abstract.lower():
            connection_type = "extends"
        
        description = f"Shares {len(overlap)} concepts: {', '.join(list(overlap)[:5])}"
        
        connections.append(SynthesisConnection(
            related_packet_id=other_packet['packet_id'],
            connection_type=connection_type,
            strength=strength,
            description=description
        ))
    
    connections.sort(key=lambda c: c.strength, reverse=True)
    return connections[:5]


# ============================================================================
# ROUTING
# ============================================================================

def route_research(packet: ResearchPacket) -> Tuple[RoutingDecision, float, str]:
    """Route research packet with priority and explanation."""
    
    explanation_parts = []
    
    theoretical_score = packet.theoretical.score if packet.theoretical else 0.0
    empirical_score = (
        sum(e.support_level for e in packet.empirical) / len(packet.empirical)
        if packet.empirical else 0.0
    )
    novelty_score = packet.novelty.score if packet.novelty else 0.0
    impact_score = packet.impact.potential if packet.impact else 0.0
    mission_score = packet.impact.mission_alignment if packet.impact else 0.0
    
    breakthrough = (
        packet.theoretical.breakthrough_potential > 0.7
        if packet.theoretical else False
    )
    paradigm_shift = packet.novelty.paradigm_shift if packet.novelty else False
    
    has_issues = (
        len(packet.theoretical.issues) > 0 if packet.theoretical else False
    )
    has_contradictions = any(len(e.contradictions) > 0 for e in packet.empirical)
    
    strong_connections = len([s for s in packet.synthesis if s.strength > 0.6])
    
    # Mission-critical
    if mission_score > 0.8:
        priority = 1.0 if mission_score > 0.9 else 0.95
        explanation_parts.append(f"Mission alignment {mission_score:.2f}")
        return RoutingDecision.MISSION_CRITICAL, priority, " | ".join(explanation_parts)
    
    # Review needed
    if has_issues or has_contradictions:
        priority = 0.9
        if has_issues:
            explanation_parts.append("Theoretical issues detected")
        if has_contradictions:
            explanation_parts.append("Empirical contradictions found")
        return RoutingDecision.REVIEW_NEEDED, priority, " | ".join(explanation_parts)
    
    # Active development
    if (theoretical_score > 0.8 and novelty_score > 0.7) or breakthrough or paradigm_shift:
        priority = 0.85
        explanation_parts.append(f"High potential: Theory {theoretical_score:.2f}, Novelty {novelty_score:.2f}")
        if breakthrough:
            explanation_parts.append("⚡ Breakthrough potential")
        if paradigm_shift:
            explanation_parts.append("🌟 Paradigm shift")
        return RoutingDecision.ACTIVE_DEVELOPMENT, priority, " | ".join(explanation_parts)
    
    # Synthesis needed
    if strong_connections >= 3:
        priority = 0.75
        explanation_parts.append(f"{strong_connections} strong connections")
        return RoutingDecision.SYNTHESIS_NEEDED, priority, " | ".join(explanation_parts)
    
    # Documentation
    if empirical_score > 0.85 and theoretical_score > 0.7:
        priority = 0.7
        explanation_parts.append("Strong validation, ready to publish")
        return RoutingDecision.DOCUMENTATION, priority, " | ".join(explanation_parts)
    
    # Archive
    if packet.status == "published":
        priority = 0.3
        explanation_parts.append("Published and integrated")
        return RoutingDecision.ARCHIVE, priority, " | ".join(explanation_parts)
    
    # Default
    priority = 0.5 + (theoretical_score + novelty_score + impact_score) / 6
    explanation_parts.append("Standard development")
    return RoutingDecision.ACTIVE_DEVELOPMENT, priority, " | ".join(explanation_parts)


def create_research_glyph(title: str, research_type: str, theoretical_score: float,
                         novelty_score: float, impact_score: float) -> str:
    """Generate PICTOGRAM-256 glyph."""
    
    type_map = {
        'theory': 'T', 'validation': 'V', 'application': 'A',
        'insight': 'I', 'synthesis': 'S', 'question': 'Q', 'breakthrough': 'B'
    }
    
    glyph_1 = type_map.get(research_type.lower(), 'R')
    
    quality = (theoretical_score + novelty_score + impact_score) / 3
    quality_hex = hex(int(quality * 15))[2:].upper()
    glyph_2 = quality_hex
    
    title_hash = hashlib.sha256(title.encode()).hexdigest()
    glyph_3 = title_hash[0].upper()
    
    return f"{glyph_1}{glyph_2}{glyph_3}"


# ============================================================================
# PROCESSING
# ============================================================================

def process_research_item(title: str, abstract: str, key_findings: List[str],
                         research_type: ResearchType, source: str,
                         methodology: str = "", existing_packets: List[Dict] = None,
                         tags: List[str] = None) -> ResearchPacket:
    """Process research through 5-agent pipeline."""
    
    if existing_packets is None:
        existing_packets = []
    if tags is None:
        tags = []
    
    packet_id = str(uuid.uuid4())[:8]
    
    theoretical = theoretical_agent(title, abstract, key_findings, methodology)
    empirical = empirical_agent(title, abstract, methodology, source)
    novelty = novelty_agent(title, abstract, key_findings, existing_packets)
    impact = impact_agent(title, abstract, research_type.value, key_findings)
    synthesis = synthesis_agent(packet_id, title, abstract, key_findings, existing_packets)
    
    packet = ResearchPacket(
        packet_id=packet_id,
        title=title,
        research_type=research_type,
        timestamp=datetime.now(),
        source=source,
        abstract=abstract,
        key_findings=key_findings,
        methodology=methodology,
        tags=tags,
        theoretical=theoretical,
        empirical=[empirical],
        novelty=novelty,
        impact=impact,
        synthesis=synthesis
    )
    
    packet.chrono_marker = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    packet.pictogram_hash = create_research_glyph(
        title, research_type.value, theoretical.score, novelty.score, impact.potential
    )
    packet.vse_encoding = {
        'intent': research_type.value,
        'affect_positive': impact.potential,
        'certainty': theoretical.score,
        'temporal_marker': packet.chrono_marker
    }
    
    routing, priority, explanation = route_research(packet)
    packet.routing_decision = routing
    packet.priority_score = priority
    
    return packet


def save_database(packets: List[ResearchPacket], path: str):
    """Save packets to JSON."""
    data = []
    for p in packets:
        d = asdict(p)
        d['research_type'] = p.research_type.value
        d['routing_decision'] = p.routing_decision.value if p.routing_decision else None
        d['timestamp'] = p.timestamp.isoformat()
        if p.empirical:
            for i, e in enumerate(d['empirical']):
                e['timestamp'] = p.empirical[i].timestamp.isoformat()
        data.append(d)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def load_database(path: str) -> List[ResearchPacket]:
    """Load packets from JSON."""
    if not Path(path).exists():
        return []
    
    with open(path, 'r') as f:
        data = json.load(f)
    
    packets = []
    for d in data:
        d['research_type'] = ResearchType(d['research_type'])
        d['routing_decision'] = (
            RoutingDecision(d['routing_decision']) 
            if d['routing_decision'] else None
        )
        d['timestamp'] = datetime.fromisoformat(d['timestamp'])
        packets.append(ResearchPacket(**d))
    
    return packets


# ============================================================================
# CLI
# ============================================================================

def cmd_create(args, packets):
    """Create new research packet."""
    packet = process_research_item(
        title=args.title,
        abstract=args.abstract,
        key_findings=args.findings,
        research_type=ResearchType(args.type),
        source=args.source,
        methodology=args.methodology or "",
        existing_packets=[asdict(p) for p in packets],
        tags=args.tags or []
    )
    
    packets.append(packet)
    save_database(packets, args.database)
    
    print(f"✓ Created: {packet.packet_id}")
    print(f"  Title: {packet.title}")
    print(f"  Routing: {packet.routing_decision.value}")
    print(f"  Priority: {packet.priority_score:.2f}")


def cmd_list(args, packets):
    """List research packets."""
    filtered = packets
    
    if args.type:
        filtered = [p for p in filtered if p.research_type.value == args.type]
    
    if args.sort == 'priority':
        filtered.sort(key=lambda p: p.priority_score, reverse=True)
    elif args.sort == 'date':
        filtered.sort(key=lambda p: p.timestamp, reverse=True)
    
    filtered = filtered[:args.limit]
    
    print(f"Research Packets ({len(filtered)} shown):\n")
    for p in filtered:
        print(f"[{p.packet_id}] {p.title}")
        print(f"  Type: {p.research_type.value} | Priority: {p.priority_score:.2f}")
        print()


def cmd_stats(args, packets):
    """Show database statistics."""
    if not packets:
        print("Database is empty.")
        return
    
    print("=" * 60)
    print("ESPER-THESIS Statistics")
    print("=" * 60)
    print(f"\nTotal Packets: {len(packets)}\n")
    
    type_counts = {}
    for p in packets:
        type_counts[p.research_type.value] = type_counts.get(p.research_type.value, 0) + 1
    
    print("By Type:")
    for t, c in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {t:15s}: {c:3d}")
    
    avg_priority = sum(p.priority_score for p in packets) / len(packets)
    print(f"\nAverage Priority: {avg_priority:.2f}")


def cmd_export(args, packets):
    """Export research findings."""
    if args.format == "json":
        save_database(packets, args.output or "research.json")
        print(f"✓ Exported {len(packets)} packets to JSON")
    
    elif args.format == "markdown":
        lines = ["# Research Findings\n"]
        for p in packets:
            lines.append(f"## {p.title}")
            lines.append(f"**Type**: {p.research_type.value}")
            lines.append(f"**Priority**: {p.priority_score:.2f}\n")
            lines.append(f"{p.abstract}\n")
            lines.append("**Key Findings**:")
            for f in p.key_findings:
                lines.append(f"- {f}")
            lines.append("\n---\n")
        
        output = "\n".join(lines)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"✓ Exported to {args.output}")
        else:
            print(output)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="ESPER-THESIS: Research Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--database', default='research_db.json')
    parser.add_argument('--version', action='version', version=f'ESPER-THESIS {__version__}')
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Create
    create_p = subparsers.add_parser('create')
    create_p.add_argument('--title', required=True)
    create_p.add_argument('--type', required=True, choices=[t.value for t in ResearchType])
    create_p.add_argument('--abstract', required=True)
    create_p.add_argument('--findings', nargs='+', required=True)
    create_p.add_argument('--source', default='manual')
    create_p.add_argument('--methodology', default='')
    create_p.add_argument('--tags', nargs='*')
    
    # List
    list_p = subparsers.add_parser('list')
    list_p.add_argument('--type', choices=[t.value for t in ResearchType])
    list_p.add_argument('--sort', choices=['priority', 'date'], default='priority')
    list_p.add_argument('--limit', type=int, default=20)
    
    # Stats
    subparsers.add_parser('stats')
    
    # Export
    export_p = subparsers.add_parser('export')
    export_p.add_argument('--format', choices=['json', 'markdown'], default='json')
    export_p.add_argument('--output')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    packets = load_database(args.database)
    
    if args.command == 'create':
        cmd_create(args, packets)
    elif args.command == 'list':
        cmd_list(args, packets)
    elif args.command == 'stats':
        cmd_stats(args, packets)
    elif args.command == 'export':
        cmd_export(args, packets)


if __name__ == '__main__':
    main()
