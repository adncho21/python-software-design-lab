from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from .program import Program
from .student import Student
from .course_offering import CourseOffering

class EnumEnrollmentStatus(str, Enum):
    ENROLLED = "enrolled"
    CANCELLED = "cancelled"
    WAITLISTED = "waitlisted"

@dataclass
class CourseOfferingEnrollment:
    student: Student
    course_offering: CourseOffering
    enrollment_date: date
    status: EnumEnrollmentStatus

@dataclass
class ProgramEnrollment:
    student: Student
    program: Program
    enrollment_date: date
    status: str
    expected_graduation_term: str

