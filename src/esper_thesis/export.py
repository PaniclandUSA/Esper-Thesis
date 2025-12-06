# esper_thesis/processor.py

import hashlib
import uuid
from datetime import datetime
from typing import Dict, List, Optional

from .agents import (
    theoretical_agent,
    empirical_agent,
    novelty_agent,
    impact_agent,
    synthesis_agent,
)
from .model import ResearchPacket, ResearchType
from .router import route_research


def create_research_glyph(
    title: str,
    research_type: str,
    theoretical_score: float,
    novelty_score: float,
    impact_score: float,
) -> str:
    """Generate PICTOGRAM-256-style glyph (compact hash)."""

    type_map = {
        "theory": "T",
        "validation": "V",
        "application": "A",
        "insight": "I",
        "synthesis": "S",
        "question": "Q",
        "breakthrough": "B",
    }

    glyph_1 = type_map.get(research_type.lower(), "R")

    quality = (theoretical_score + novelty_score + impact_score) / 3.0
    quality_hex = hex(int(max(0.0, min(1.0, quality)) * 15))[2:].upper()
    glyph_2 = quality_hex

    title_hash = hashlib.sha256(title.encode("utf-8")).hexdigest()
    glyph_3 = title_hash[0].upper()

    return f"{glyph_1}{glyph_2}{glyph_3}"


def process_research_item(
    title: str,
    abstract: str,
    key_findings: List[str],
    research_type: ResearchType,
    source: str,
    methodology: str = "",
    existing_packets: Optional[List[Dict]] = None,
    tags: Optional[List[str]] = None,
) -> ResearchPacket:
    """Process research through 5-agent pipeline."""

    if existing_packets is None:
        existing_packets = []

    packet_id = str(uuid.uuid4())
    now = datetime.now()

    theoretical = theoretical_agent(title, abstract, key_findings, methodology)

    empirical = empirical_agent(
        abstract=abstract,
        validation_type="ai_system",
        source=source,
    )

    novelty = novelty_agent(
        title=title,
        abstract=abstract,
        research_type=research_type.value,
        key_findings=key_findings,
        existing_packets=existing_packets,
    )

    impact = impact_agent(
        title=title,
        abstract=abstract,
        research_type=research_type.value,
        key_findings=key_findings,
    )

    synthesis = synthesis_agent(
        packet_id=packet_id,
        title=title,
        abstract=abstract,
        key_findings=key_findings,
        existing_packets=existing_packets,
    )

    packet = ResearchPacket(
        packet_id=packet_id,
        title=title,
        research_type=research_type,
        timestamp=now,
        source=source,
        abstract=abstract,
        key_findings=key_findings,
        methodology=methodology,
        tags=tags or [],
        theoretical=theoretical,
        empirical=[empirical],
        novelty=novelty,
        impact=impact,
        synthesis=synthesis,
    )

    packet.chrono_marker = now.strftime("%Y-%m-%d_%H%M%S")
    packet.pictogram_hash = create_research_glyph(
        title, research_type.value, theoretical.score, novelty.score, impact.potential
    )
    packet.vse_encoding = {
        "intent": research_type.value,
        "affect_positive": impact.potential,
        "certainty": theoretical.score,
        "temporal_marker": packet.chrono_marker,
    }

    routing, priority, _ = route_research(packet)
    packet.routing_decision = routing
    packet.priority_score = priority

    return packet
