# esper_thesis/model.py

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


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
    ARCHIVE = "archive"
    DOCUMENTATION = "documentation"
    BACKLOG = "backlog"
    DROP = "drop"


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
    innovation_vector: List[str]
    domain_span: List[str]
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
