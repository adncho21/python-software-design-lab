from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from .person import Person


class InstructorTitle(str, Enum):
    PROFESSOR = "professor"
    ASSISTANT_PROFESSOR = "assistant professor"
    LECTURER = "lecturer"


class EnumInstructorStatus(str, Enum):
    ACTIVE = "active"
    RETIRED = "retired"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"


@dataclass
class Instructor(Person):
    instructor_id: str
    title: InstructorTitle
    department: str
    salary: int
    experience: int
    status: EnumInstructorStatus | None = None
    hire_date: date | None = None
    termination_date: date | None = None
    certifications: list[str] = field(default_factory=list)
