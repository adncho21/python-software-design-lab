from dataclasses import dataclass

from models.assessment import Assessment
from models.enrollment import CourseOfferingEnrollment


@dataclass
class Grade:
    enrollment: CourseOfferingEnrollment
    assessment: Assessment
    score: float