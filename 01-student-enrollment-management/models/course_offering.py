from dataclasses import dataclass, field
from datetime import date, datetime

from .assessment import Assessment, AssessmentType
from .course import Course
from .academic_term import AcademicTerm
from .facilities import ClassRoom
from .instructor import Instructor


@dataclass
class ClassSession:
    start_at: datetime
    end_at: datetime
    room: ClassRoom


@dataclass
class CourseOffering:
    course: Course
    academic_term: AcademicTerm
    section: str
    room: ClassRoom | None = None
    instructor: Instructor | None = None
    capacity: int = 0
    waiting_list_capacity: int = 0
    class_sessions: list[ClassSession] = field(default_factory=list)
    assessments: list[Assessment] = field(default_factory=list)


    @property
    def exams(self) -> list[Assessment]:
        return [
            assessment for assessment in self.assessments
            if assessment.assessment_type in {AssessmentType.MIDTERM, AssessmentType.FINAL}
        ]
