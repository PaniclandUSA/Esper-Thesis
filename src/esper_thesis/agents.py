# esper_thesis/agents.py

import re
from datetime import datetime
from typing import Dict, List

from .model import (
    TheoreticalAssessment,
    EmpiricalEvidence,
    NoveltyRating,
    ImpactAnalysis,
    SynthesisConnection,
)


def theoretical_agent(
    title: str,
    abstract: str,
    key_findings: List[str],
    methodology: str,
) -> TheoreticalAssessment:
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
    if len(abstract.split(".")) >= 3:
        clarity_score += 0.1
    if len(key_findings) >= 2:
        clarity_score += 0.1

    breakthrough_keywords = [
        "first", "novel", "unprecedented", "breakthrough", "new paradigm", "revolutionary"
    ]
    breakthrough_score = 0.3
    text = (title + " " + abstract).lower()
    for keyword in breakthrough_keywords:
        if keyword in text:
            breakthrough_score += 0.15
    breakthrough_score = min(1.0, breakthrough_score)

    dependencies: List[str] = []
    dep_patterns = [r"requires (\w+)", r"depends on (\w+)", r"assumes (\w+)"]
    for pattern in dep_patterns:
        matches = re.findall(pattern, abstract.lower())
        dependencies.extend(matches)

    issues: List[str] = []
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
        dependencies=dependencies,
        issues=issues,
        notes="Based on abstract + key findings heuristic analysis",
    )


def empirical_agent(
    abstract: str,
    validation_type: str,
    source: str,
) -> EmpiricalEvidence:
    """Assess empirical support level."""

    base_support = 0.4
    if "experiment" in abstract.lower():
        base_support += 0.2
    if "field test" in abstract.lower():
        base_support += 0.2
    if "replicated" in abstract.lower() or "reproduced" in abstract.lower():
        base_support += 0.2

    support_level = min(1.0, base_support)

    if validation_type == "ai_system":
        support_level = max(support_level, 0.7)
    elif validation_type == "experiment":
        support_level = max(support_level, 0.8)
    elif validation_type == "field_test":
        support_level = max(support_level, 0.9)

    reproducible = (
        "reproducible" in abstract.lower() or "replicated" in abstract.lower()
    )

    contradictions: List[str] = []
    if "inconsistent" in abstract.lower():
        contradictions.append("Inconsistency noted in abstract")

    return EmpiricalEvidence(
        support_level=support_level,
        validation_type=validation_type,
        validating_system=source,
        timestamp=datetime.now(),
        description="Heuristic empirical assessment from abstract",
        reproducible=reproducible,
        contradictions=contradictions,
    )


def novelty_agent(
    title: str,
    abstract: str,
    research_type: str,
    key_findings: List[str],
    existing_packets: List[Dict],
) -> NoveltyRating:
    """Assess originality and innovation."""

    text = (title + " " + abstract).lower()
    novelty_score = 0.5

    if "first" in text or "novel" in text or "unique" in text:
        novelty_score += 0.2
    if research_type == "breakthrough":
        novelty_score += 0.2

    mission_keywords = ["literacy", "reading", "comprehension"]
    mission_boost = any(k in text for k in mission_keywords)
    if mission_boost:
        novelty_score += 0.05

    innovation_vector: List[str] = []
    domains: List[str] = []
    domain_markers = {
        "ai": "ai",
        "machine learning": "ai",
        "education": "education",
        "pedagogy": "education",
        "cognitive": "cognitive_science",
        "neuroscience": "neuroscience",
    }

    for marker, domain in domain_markers.items():
        if marker in text and domain not in domains:
            domains.append(domain)

    if len(domains) >= 3:
        novelty_score += 0.1
        innovation_vector.append("cross_domain")

    similar_packets: List[str] = []
    for packet in existing_packets:
        other_text = (
            packet.get("title", "") + " " + packet.get("abstract", "")
        ).lower()
        shared_tokens = set(text.split()) & set(other_text.split())
        if len(shared_tokens) > 5:
            similar_packets.append(packet["packet_id"])

    if len(similar_packets) > 3:
        novelty_score *= 0.8

    unique_contributions: List[str] = []
    for finding in key_findings:
        if any(marker in finding.lower() for marker in ["first", "only", "unique", "novel"]):
            unique_contributions.append(finding)

    if not unique_contributions:
        unique_contributions = key_findings[:2]

    comparison = "This work"
    if similar_packets:
        comparison += f" builds on {len(similar_packets)} related findings"
    else:
        comparison += " appears distinct in the current corpus"

    paradigm_shift = "paradigm" in text or "fundamental" in text

    return NoveltyRating(
        score=min(1.0, novelty_score),
        innovation_vector=innovation_vector or ["incremental"],
        domain_span=domains or ["unspecified"],
        paradigm_shift=paradigm_shift,
        lineage=similar_packets[:5],
        notes=f"{comparison}; unique contributions: {', '.join(unique_contributions)}",
    )


def impact_agent(
    title: str,
    abstract: str,
    research_type: str,
    key_findings: List[str],
) -> ImpactAnalysis:
    """Measure significance and potential reach."""

    text = (title + " " + abstract).lower()

    academic_keywords = [
        "theory", "framework", "model", "hypothesis", "validation",
        "empirical", "research", "study",
    ]
    industry_keywords = [
        "deployment", "production", "tooling", "platform", "pipeline", "rollout",
    ]
    mission_keywords = ["literacy", "reading", "comprehension", "students", "learners"]

    academic_score = 0.4 + 0.05 * sum(k in text for k in academic_keywords)
    industry_score = 0.3 + 0.07 * sum(k in text for k in industry_keywords)
    mission_score = 0.3 + 0.1 * sum(k in text for k in mission_keywords)

    domains: List[str] = []
    for word in text.split():
        if word.endswith("tech") or word.endswith("stack"):
            if "technology" not in domains:
                domains.append("technology")
        if word in {"teacher", "classroom", "school"}:
            if "education" not in domains:
                domains.append("education")

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

    notes: List[str] = []
    if mission_score > 0.7:
        notes.append("Strong mission alignment - direct literacy impact")
    if research_type == "breakthrough":
        notes.append("Marked as breakthrough; prioritize review")

    return ImpactAnalysis(
        potential=min(1.0, impact_potential),
        academic_impact=min(1.0, academic_score),
        industry_application=min(1.0, industry_score),
        mission_alignment=min(1.0, mission_score),
        cross_domain_reach=domains,
        timeline_to_impact=timeline,
        notes=" | ".join(notes) if notes else "",
    )


def synthesis_agent(
    packet_id: str,
    title: str,
    abstract: str,
    key_findings: List[str],
    existing_packets: List[Dict],
) -> List[SynthesisConnection]:
    """Discover connections between research packets."""

    connections: List[SynthesisConnection] = []

    my_keywords = {
        word.lower()
        for word in (title + " " + abstract).split()
        if len(word) > 4 and word.isalnum()
    }

    for other_packet in existing_packets:
        if other_packet.get("packet_id") == packet_id:
            continue

        other_text = (
            other_packet.get("title", "") + " " + other_packet.get("abstract", "")
        )
        other_keywords = {
            word.lower()
            for word in other_text.split()
            if len(word) > 4 and word.isalnum()
        }

        overlap = my_keywords & other_keywords
        if len(overlap) < 2:
            continue

        strength = min(1.0, len(overlap) / 10.0)
        related_id = other_packet["packet_id"]

        description = f"Shares {len(overlap)} key terms with packet {related_id}"
        conn_type = "related"
        if "method" in other_text.lower() or "framework" in other_text.lower():
            conn_type = "builds_on"

        connections.append(
            SynthesisConnection(
                related_packet_id=related_id,
                connection_type=conn_type,
                strength=strength,
                description=description,
            )
        )

    return connections
