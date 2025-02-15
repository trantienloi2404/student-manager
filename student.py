import re
from datetime import datetime

# Constants
FACULTIES = [
    "Khoa Luật",
    "Khoa Tiếng Anh thương mại",
    "Khoa Tiếng Nhật",
    "Khoa Tiếng Pháp",
]
STATUSES = ["Đang học", "Đã tốt nghiệp", "Đã thôi học", "Tạm dừng học"]
GENDERS = ["Nam", "Nữ", "Khác"]


# Student class
class Student:
    def __init__(
        self,
        mssv,
        name,
        dob,
        gender,
        faculty,
        year,
        program,
        address,
        email,
        phone,
        status,
    ):
        self.mssv = mssv
        self.name = name
        self.dob = dob
        self.gender = gender
        self.faculty = faculty
        self.year = year
        self.program = program
        self.address = address
        self.email = email
        self.phone = phone
        self.status = status

    def __str__(self):
        return (
            f"MSSV: {self.mssv}, Name: {self.name}, DOB: {self.dob}, Gender: {self.gender}, "
            f"Faculty: {self.faculty}, Year: {self.year}, Program: {self.program}, Address: {self.address}, "
            f"Email: {self.email}, Phone: {self.phone}, Status: {self.status}"
        )


# Validation functions
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def validate_phone(phone):
    pattern = r"^\d{10}$"
    return re.match(pattern, phone) is not None


def validate_faculty(faculty):
    return faculty in FACULTIES


def validate_status(status):
    return status in STATUSES


def validate_dob(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_year(year):
    try:
        year = int(year)
        return 1900 <= year <= datetime.now().year
    except ValueError:
        return False


def validate_gender(gender):
    return gender in GENDERS
