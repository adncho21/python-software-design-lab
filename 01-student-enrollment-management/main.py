from dataclasses import dataclass, field
from enum import Enum


class EnumGender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


@dataclass
class AcademicTerm:
    year: int
    season: str
    start_date: str
    end_date: str


@dataclass
class Building:
    code: str
    name: str
    location: str


@dataclass
class classRoom:
    code: str
    name: str
    capacity: int
    building: Building


@dataclass
class Course:
    course_id: str
    course_name: str
    subjects: list[str]
    program: str
    location: str
    instruction_mode: str
    credits: int


@dataclass
class CourseOffering:
    course: Course
    academic_term: AcademicTerm
    class_name: str = None
    room: classRoom = None
    instructor: str = None
    capacity: int = None
    waiting_list_capacity: int = None
    enrolled_students: list[str] = None
    waitlist: list[str] = None


    @property
    def available_seats(self):
        return self.capacity - len(self.enrolled_students)


    @property
    def waitlist_total(self):
        return len(self.waitlist)


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
    gender: EnumGender
    date_of_birth: str
    nationality: str = None
    emergency_contact_name: str = None
    emergency_contact_phone_number: str = None
    emergency_contact_relationship: str = None
    emergency_contact_email: str = None
    emergency_contact_address: Address = None


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


@dataclass
class Student(Person):
    student_id: str


@dataclass
class Instructor(Person):
    instructor_id: str
    course_offerings: list[CourseOffering] = field(default_factory=list)


def main():
    student_address = Address(
        street="2151 St-trinty street #14",
        city="Montreal",
        state="QC",
        zip_code="H1X 5D2",
        country="Canada"
    )
    student = Student(
        student_id="123456789",
        first_name="John",
        last_name="Walter",
        email="john.walter@gmail.com",
        phone_number="123-456-7890",
        address=student_address,
        gender=EnumGender.MALE,
        date_of_birth="1990-05-12"
    )

    course_offering = CourseOffering(
        course=Course(
            course_id="CS101",
            course_name="Introduction to Computer Science",
            subjects=["Data Structures", "Algorithms"],
            program="Bachelor of Science in Computer Science",
            location="City University of New York",
            instruction_mode="Online",
            credits=3
        ),
        academic_term=AcademicTerm(
            year=2026,
            season="Fall",
            start_date="2024-08-23",
            end_date="2024-12-31"
        ))

    print(student)
    #print(course_offering)


if __name__ == "__main__":
    main()
