from dataclasses import dataclass

from .assessment import Assessment
from .enrollment import CourseEnrollment


@dataclass
class Grade:
    enrollment: CourseEnrollment
    assessment: Assessment
    score: float