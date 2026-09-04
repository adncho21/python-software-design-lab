from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum

from .assessment import Assessment, EnumAssessmentType
from .course import Course
from .academic_term import AcademicTerm
from .facilities import ClassRoom
from .instructor import Instructor


@dataclass
class ClassSession:
    class_date: date
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
    exams: list[Assessment] = field(default_factory=list)

    def add_exam(self, exam: Assessment) -> None:
        if exam.assessment_type not in {
            EnumAssessmentType.MIDTERM,
            EnumAssessmentType.FINAL,
        }:
            raise ValueError(
                "Only midterm and final assessments can be added as exams."
            )

        self.exams.append(exam)
