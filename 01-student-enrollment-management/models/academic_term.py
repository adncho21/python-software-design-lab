from dataclasses import dataclass
from datetime import date
from enum import Enum

class AcademicSeason(Enum):
    FALL = "fall"
    SUMMER = "summer"
    WINTER = "winter"

@dataclass
class AcademicTerm:
    year: int
    season: AcademicSeason
    start_date: date
    end_date: date
