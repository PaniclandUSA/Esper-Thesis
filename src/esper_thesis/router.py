# esper_thesis/router.py

from typing import Tuple

from .model import ResearchPacket, RoutingDecision


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

    # Mission-aligned breakthroughs → active development
    if breakthrough and mission_score > 0.6:
        explanation_parts.append("High theoretical breakthrough + strong mission alignment")
        priority = 0.95
        return RoutingDecision.ACTIVE_DEVELOPMENT, priority, " | ".join(explanation_parts)

    # Paradigm shift but weak validation → synthesis needed
    if paradigm_shift and empirical_score < 0.5:
        explanation_parts.append("Paradigm-shift claim needs synthesis & validation")
        priority = 0.85
        return RoutingDecision.SYNTHESIS_NEEDED, priority, " | ".join(explanation_parts)

    # Low scores or explicit issues → backlog or drop
    if theoretical_score < 0.3 and empirical_score < 0.3:
        explanation_parts.append("Low theoretical and empirical scores")
        priority = 0.2
        return RoutingDecision.BACKLOG, priority, " | ".join(explanation_parts)

    if has_issues and impact_score < 0.4:
        explanation_parts.append("Issues detected with limited impact")
        priority = 0.1
        return RoutingDecision.DROP, priority, " | ".join(explanation_parts)

    # Documentation: strong validation + decent theory
    if empirical_score > 0.85 and theoretical_score > 0.7:
        explanation_parts.append("Strong validation, ready to document/publish")
        priority = 0.7
        return RoutingDecision.DOCUMENTATION, priority, " | ".join(explanation_parts)

    # Archive: published work
    if packet.status == "published":
        explanation_parts.append("Published and integrated; safe to archive")
        priority = 0.3
        return RoutingDecision.ARCHIVE, priority, " | ".join(explanation_parts)

    # Default active development
    priority = 0.5 + (theoretical_score + novelty_score + impact_score) / 6.0
    explanation_parts.append("Standard development")
    return RoutingDecision.ACTIVE_DEVELOPMENT, priority, " | ".join(explanation_parts)
