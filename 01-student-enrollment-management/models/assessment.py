from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from .facilities import ClassRoom


class AssessmentType(Enum):
    ASSIGNMENT = "assignment"
    MIDTERM = "midterm"
    FINAL = "final"
    PROJECT = "project"


@dataclass
class Assessment:
    name: str
    assessment_type: AssessmentType
    weight: float
    max_score: float
    start_at: datetime | None = None
    end_at: datetime | None = None
    room: ClassRoom | None = None
    is_group_work: bool = False
