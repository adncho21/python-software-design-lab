from dataclasses import dataclass, field
from enum import Enum

class EnumInstructionMode(Enum):
    ONLINE = "online"
    IN_PERSON = "in-person"
    HYBRID = "hybrid"
    OTHER = "other"

@dataclass
class Course:
    course_id: str
    course_name: str
    subjects: list[str]
    program: str
    location: str
    credits: int
    instruction_modes: list[EnumInstructionMode] = field(default_factory=list)
