# esper_thesis/storage.py

import json
from datetime import datetime
from pathlib import Path
from typing import List

from dataclasses import asdict

from .model import ResearchPacket, ResearchType, RoutingDecision


def save_database(packets: List[ResearchPacket], path: Path) -> None:
    """Save packets to JSON."""
    data = []
    for p in packets:
        d = asdict(p)
        d["research_type"] = p.research_type.value
        d["routing_decision"] = (
            p.routing_decision.value if p.routing_decision else None
        )
        d["timestamp"] = p.timestamp.isoformat()
        if p.empirical:
            for i, e in enumerate(d["empirical"]):
                e["timestamp"] = p.empirical[i].timestamp.isoformat()
        data.append(d)

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_database(path: Path) -> List[ResearchPacket]:
    """Load packets from JSON."""
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    packets: List[ResearchPacket] = []
    for d in data:
        d["research_type"] = ResearchType(d["research_type"])
        d["routing_decision"] = (
            RoutingDecision(d["routing_decision"]) if d["routing_decision"] else None
        )
        d["timestamp"] = datetime.fromisoformat(d["timestamp"])
        packets.append(ResearchPacket(**d))

    return packets
