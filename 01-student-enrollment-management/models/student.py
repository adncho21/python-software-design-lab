from dataclasses import dataclass
from .person import Person

@dataclass
class Student(Person):
    student_id: str
