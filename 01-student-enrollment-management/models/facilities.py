from dataclasses import dataclass


@dataclass
class Building:
    code: str
    name: str
    location: str


@dataclass
class ClassRoom:
    code: str
    name: str
    capacity: int
    building: Building
