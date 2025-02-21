import csv
import os
import json  # For JSON operations
import logging  # For logging mechanism
from student import (
    Student,
    FACULTIES,
    STATUSES,
    PROGRAMS,
    validate_email,
    validate_phone,
    validate_faculty,
    validate_status,
    validate_dob,
    validate_year,
    validate_gender,
    validate_program,
)


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_from_csv()  # Auto-load CSV data if available
        logging.info("StudentManager initialized and data loaded from CSV (if exists).")

    def add_student(self):
        print("Add a new student:")
        mssv = input("MSSV: ")
        name = input("Name: ")
        dob = input("DOB (YYYY-MM-DD): ")
        while not validate_dob(dob):
            print("Invalid date of birth. Please use the format YYYY-MM-DD.")
            dob = input("DOB (YYYY-MM-DD): ")
        gender = input("Gender (Nam/Nữ/Khác): ")
        while not validate_gender(gender):
            print("Invalid gender. Please choose from: Nam, Nữ, Khác.")
            gender = input("Gender (Nam/Nữ/Khác): ")
        faculty = input("Faculty: ")
        while not validate_faculty(faculty):
            print("Invalid faculty. Please choose from: ", FACULTIES)
            faculty = input("Faculty: ")
        year = input("Year: ")
        while not validate_year(year):
            print("Invalid year. Please enter a valid year (1900-current year).")
            year = input("Year: ")

        # Select program from list or add new one
        print("Available Programs: ", PROGRAMS)
        program = input(
            "Select a program from the list or type 'new' to add a new program: "
        )
        if program.lower() == "new":
            new_program = input("Enter new program name: ")
            PROGRAMS.append(new_program)
            program = new_program
        else:
            while program not in PROGRAMS:
                print("Invalid program. Available options: ", PROGRAMS)
                program = input(
                    "Select a program from the list or type 'new' to add a new program: "
                )
                if program.lower() == "new":
                    new_program = input("Enter new program name: ")
                    PROGRAMS.append(new_program)
                    program = new_program
                    break

        address = input("Address: ")
        email = input("Email: ")
        while not validate_email(email):
            print("Invalid email format. Please enter a valid email.")
            email = input("Email: ")
        phone = input("Phone: ")
        while not validate_phone(phone):
            print("Invalid phone number. Please enter a 10-digit number.")
            phone = input("Phone: ")
        status = input("Status: ")
        while not validate_status(status):
            print("Invalid status. Please choose from: ", STATUSES)
            status = input("Status: ")

        student = Student(
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
        )
        self.students.append(student)
        print("Student added successfully!")
        logging.info("Added new student: MSSV=%s, Name=%s", mssv, name)
        self.save_to_csv()  # Auto-save after adding a student

    def delete_student(self):
        mssv = input("Enter MSSV to delete: ")
        for student in self.students:
            if student.mssv == mssv:
                self.students.remove(student)
                print("Student deleted successfully!")
                logging.info("Deleted student with MSSV=%s", mssv)
                self.save_to_csv()  # Auto-save after deleting a student
                return
        print("Student not found.")
        logging.warning("Attempted to delete non-existent student with MSSV=%s", mssv)

    def update_student(self):
        mssv = input("Enter MSSV to update: ")
        for student in self.students:
            if student.mssv == mssv:
                print("Update student information:")
                student.name = input(f"Name ({student.name}): ") or student.name
                dob = input(f"DOB ({student.dob}): ") or student.dob
                while not validate_dob(dob):
                    print("Invalid date of birth. Please use the format YYYY-MM-DD.")
                    dob = input(f"DOB ({student.dob}): ") or student.dob
                student.dob = dob
                gender = input(f"Gender ({student.gender}): ") or student.gender
                while not validate_gender(gender):
                    print("Invalid gender. Please choose from: Nam, Nữ, Khác.")
                    gender = input(f"Gender ({student.gender}): ") or student.gender
                student.gender = gender
                faculty = input(f"Faculty ({student.faculty}): ") or student.faculty
                while not validate_faculty(faculty):
                    print("Invalid faculty. Please choose from: ", FACULTIES)
                    faculty = input(f"Faculty ({student.faculty}): ") or student.faculty
                student.faculty = faculty
                year = input(f"Year ({student.year}): ") or student.year
                while not validate_year(year):
                    print(
                        "Invalid year. Please enter a valid year (1900-current year)."
                    )
                    year = input(f"Year ({student.year}): ") or student.year
                student.year = year

                # Update program with selection from list or adding new
                print("Available Programs: ", PROGRAMS)
                program_input = (
                    input(f"Program ({student.program}): ") or student.program
                )
                if program_input.lower() == "new":
                    new_program = input("Enter new program name: ")
                    PROGRAMS.append(new_program)
                    program_input = new_program
                else:
                    while program_input not in PROGRAMS:
                        print("Invalid program. Available options: ", PROGRAMS)
                        program_input = (
                            input(f"Program ({student.program}): ") or student.program
                        )
                        if program_input.lower() == "new":
                            new_program = input("Enter new program name: ")
                            PROGRAMS.append(new_program)
                            program_input = new_program
                            break
                student.program = program_input

                student.address = (
                    input(f"Address ({student.address}): ") or student.address
                )
                email = input(f"Email ({student.email}): ") or student.email
                while not validate_email(email):
                    print("Invalid email format. Please enter a valid email.")
                    email = input(f"Email ({student.email}): ") or student.email
                student.email = email
                phone = input(f"Phone ({student.phone}): ") or student.phone
                while not validate_phone(phone):
                    print("Invalid phone number. Please enter a 10-digit number.")
                    phone = input(f"Phone ({student.phone}): ") or student.phone
                student.phone = phone
                status = input(f"Status ({student.status}): ") or student.status
                while not validate_status(status):
                    print("Invalid status. Please choose from: ", STATUSES)
                    status = input(f"Status ({student.status}): ") or student.status
                student.status = status
                print("Student updated successfully!")
                logging.info("Updated student: MSSV=%s", mssv)
                self.save_to_csv()  # Auto-save after updating a student
                return
        print("Student not found.")
        logging.warning("Attempted to update non-existent student with MSSV=%s", mssv)

    def search_student(self):
        print("\nSearch Student")
        print("1. Search by MSSV or Name")
        print("2. Search by Faculty")
        print("3. Search by Faculty and Student Name")
        choice = input("Enter your choice: ")
        if choice == "2":
            self.search_by_faculty()
        elif choice == "3":
            self.search_by_faculty_and_name()
        else:
            search_term = input("Enter MSSV or Name to search: ")
            results = []
            for student in self.students:
                if (
                    search_term.lower() in student.mssv.lower()
                    or search_term.lower() in student.name.lower()
                ):
                    results.append(student)
            if results:
                print("Search results:")
                for student in results:
                    print(student)
            else:
                print("No students found.")
            logging.info("Searched by MSSV/Name with term: %s", search_term)

    def search_by_faculty(self):
        faculty_input = input("Enter Faculty to search: ")
        results = [
            student
            for student in self.students
            if faculty_input.lower() in student.faculty.lower()
        ]
        if results:
            print("Search results (by Faculty):")
            for student in results:
                print(student)
        else:
            print("No students found for faculty:", faculty_input)
        logging.info("Searched by Faculty with term: %s", faculty_input)

    def search_by_faculty_and_name(self):
        faculty_input = input("Enter Faculty to search: ")
        name_input = input("Enter Student Name (or part of it) to search: ")
        results = [
            student
            for student in self.students
            if faculty_input.lower() in student.faculty.lower()
            and name_input.lower() in student.name.lower()
        ]
        if results:
            print("Search results (by Faculty and Name):")
            for student in results:
                print(student)
        else:
            print("No students found for the given faculty and name combination.")
        logging.info("Searched by Faculty: %s and Name: %s", faculty_input, name_input)

    def list_students(self):
        if not self.students:
            print("No students in the list.")
        else:
            print("List of students:")
            for student in self.students:
                print(student)
        logging.info("Listed all students. Count: %d", len(self.students))

    def save_to_csv(self, filename="students.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "mssv",
                "name",
                "dob",
                "gender",
                "faculty",
                "year",
                "program",
                "address",
                "email",
                "phone",
                "status",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow(
                    {
                        "mssv": student.mssv,
                        "name": student.name,
                        "dob": student.dob,
                        "gender": student.gender,
                        "faculty": student.faculty,
                        "year": student.year,
                        "program": student.program,
                        "address": student.address,
                        "email": student.email,
                        "phone": student.phone,
                        "status": student.status,
                    }
                )
        print("Exported students to CSV.")
        logging.info(
            "Exported %d students to CSV file: %s", len(self.students), filename
        )

    def load_from_csv(self, filename="students.csv"):
        self.students.clear()
        if os.path.exists(filename):
            with open(filename, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student = Student(
                        row["mssv"],
                        row["name"],
                        row["dob"],
                        row["gender"],
                        row["faculty"],
                        row["year"],
                        row["program"],
                        row["address"],
                        row["email"],
                        row["phone"],
                        row["status"],
                    )
                    self.students.append(student)
            print("Imported students from CSV.")
            logging.info(
                "Imported %d students from CSV file: %s", len(self.students), filename
            )
        else:
            print("CSV file not found.")
            logging.warning("CSV file not found for import: %s", filename)

    def export_to_json(self, filename="students.json"):
        data = []
        for student in self.students:
            data.append(
                {
                    "mssv": student.mssv,
                    "name": student.name,
                    "dob": student.dob,
                    "gender": student.gender,
                    "faculty": student.faculty,
                    "year": student.year,
                    "program": student.program,
                    "address": student.address,
                    "email": student.email,
                    "phone": student.phone,
                    "status": student.status,
                }
            )
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        print("Exported students to JSON.")
        logging.info(
            "Exported %d students to JSON file: %s", len(self.students), filename
        )

    def import_from_json(self, filename="students.json"):
        if os.path.exists(filename):
            with open(filename, encoding="utf-8") as jsonfile:
                data = json.load(jsonfile)
            self.students.clear()
            for row in data:
                student = Student(
                    row["mssv"],
                    row["name"],
                    row["dob"],
                    row["gender"],
                    row["faculty"],
                    row["year"],
                    row["program"],
                    row["address"],
                    row["email"],
                    row["phone"],
                    row["status"],
                )
                self.students.append(student)
            print("Imported students from JSON.")
            logging.info(
                "Imported %d students from JSON file: %s", len(self.students), filename
            )
        else:
            print("JSON file does not exist.")
            logging.warning("JSON file not found for import: %s", filename)

    # The management functions for Faculties, Statuses, and Programs remain unchanged.
    def manage_faculties(self):
        while True:
            print("\nManage Faculties")
            print("1. Add new Faculty")
            print("2. Rename existing Faculty")
            print("3. List Faculties")
            print("4. Back to main menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_faculty = input("Enter new Faculty name: ")
                if new_faculty in FACULTIES:
                    print("Faculty already exists.")
                else:
                    FACULTIES.append(new_faculty)
                    print("New Faculty added.")
                    logging.info("Added new Faculty: %s", new_faculty)
            elif choice == "2":
                print("Existing Faculties: ", FACULTIES)
                old_name = input("Enter the Faculty name to rename: ")
                if old_name not in FACULTIES:
                    print("Faculty not found.")
                else:
                    new_name = input("Enter new Faculty name: ")
                    index = FACULTIES.index(old_name)
                    FACULTIES[index] = new_name
                    for student in self.students:
                        if student.faculty == old_name:
                            student.faculty = new_name
                    print("Faculty renamed successfully.")
                    logging.info("Renamed Faculty from %s to %s", old_name, new_name)
            elif choice == "3":
                print("List of Faculties: ", FACULTIES)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    def manage_statuses(self):
        while True:
            print("\nManage Student Statuses")
            print("1. Add new Status")
            print("2. Rename existing Status")
            print("3. List Statuses")
            print("4. Back to main menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_status = input("Enter new Status: ")
                if new_status in STATUSES:
                    print("Status already exists.")
                else:
                    STATUSES.append(new_status)
                    print("New Status added.")
                    logging.info("Added new Status: %s", new_status)
            elif choice == "2":
                print("Existing Statuses: ", STATUSES)
                old_status = input("Enter the Status to rename: ")
                if old_status not in STATUSES:
                    print("Status not found.")
                else:
                    new_status = input("Enter new Status name: ")
                    index = STATUSES.index(old_status)
                    STATUSES[index] = new_status
                    for student in self.students:
                        if student.status == old_status:
                            student.status = new_status
                    print("Status renamed successfully.")
                    logging.info("Renamed Status from %s to %s", old_status, new_status)
            elif choice == "3":
                print("List of Statuses: ", STATUSES)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    def manage_programs(self):
        while True:
            print("\nManage Programs")
            print("1. Add new Program")
            print("2. Rename existing Program")
            print("3. List Programs")
            print("4. Back to main menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_program = input("Enter new Program name: ")
                if new_program in PROGRAMS:
                    print("Program already exists.")
                else:
                    PROGRAMS.append(new_program)
                    print("New Program added.")
                    logging.info("Added new Program: %s", new_program)
            elif choice == "2":
                print("Existing Programs: ", PROGRAMS)
                old_program = input("Enter the Program to rename: ")
                if old_program not in PROGRAMS:
                    print("Program not found.")
                else:
                    new_program = input("Enter new Program name: ")
                    index = PROGRAMS.index(old_program)
                    PROGRAMS[index] = new_program
                    for student in self.students:
                        if student.program == old_program:
                            student.program = new_program
                    print("Program renamed successfully.")
                    logging.info(
                        "Renamed Program from %s to %s", old_program, new_program
                    )
            elif choice == "3":
                print("List of Programs: ", PROGRAMS)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")
