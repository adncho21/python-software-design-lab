from dataclasses import dataclass

from models.assessment import Assessment
from models.courseofferingenrollment import CourseOfferingEnrollment


@dataclass
class Grade:
    enrollment: CourseOfferingEnrollment
    assessment: Assessment
    score: float