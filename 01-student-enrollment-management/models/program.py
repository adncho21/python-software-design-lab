from dataclasses import dataclass, field

from models.course import Course


@dataclass
class Program:
    code: str
    name: str
    total_credits: int
    required_courses: list[Course] = field(default_factory=list)
    elective_courses: list[Course] = field(default_factory=list)


