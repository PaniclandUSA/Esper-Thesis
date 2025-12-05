# esper_thesis/__init__.py

from .config import __version__
from .model import (
    ResearchType,
    RoutingDecision,
    TheoreticalAssessment,
    EmpiricalEvidence,
    NoveltyRating,
    ImpactAnalysis,
    SynthesisConnection,
    ResearchPacket,
)
from .processor import process_research_item

__all__ = [
    "__version__",
    "ResearchType",
    "RoutingDecision",
    "TheoreticalAssessment",
    "EmpiricalEvidence",
    "NoveltyRating",
    "ImpactAnalysis",
    "SynthesisConnection",
    "ResearchPacket",
    "process_research_item",
]
