from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


@dataclass
class Address:
    street: str
    city: str
    state: str
    zip_code: str
    country: str


@dataclass(kw_only=True)
class Person:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: Address
    gender: Gender
    date_of_birth: date

    # Optional fields
    nationality: str = None
    emergency_contact_name: str = None
    emergency_contact_phone_number: str = None
    emergency_contact_relationship: str = None
    emergency_contact_email: str = None
    emergency_contact_address: Address = None


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
