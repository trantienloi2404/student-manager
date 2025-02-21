import csv
import os
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
        self.load_from_csv()  # Load existing data from CSV file if available

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

        # New: Select program from list or add new one
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
        self.save_to_csv()  # Auto-save after adding a student

    def delete_student(self):
        mssv = input("Enter MSSV to delete: ")
        for student in self.students:
            if student.mssv == mssv:
                self.students.remove(student)
                print("Student deleted successfully!")
                self.save_to_csv()  # Auto-save after deleting a student
                return
        print("Student not found.")

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

                # New: Update program with selection from list or adding new
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
                self.save_to_csv()  # Auto-save after updating a student
                return
        print("Student not found.")

    def search_student(self):
        search_term = input("Enter MSSV or name to search: ")
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

    def list_students(self):
        if not self.students:
            print("No students in the list.")
        else:
            print("List of students:")
            for student in self.students:
                print(student)

    def save_to_csv(self, filename="students.csv"):
        # Save student data to a CSV file
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
        print("Saved students to CSV.")

    def load_from_csv(self, filename="students.csv"):
        # Load student data from a CSV file if it exists
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
            print("Loaded students from CSV.")

    # New: Function to manage Faculties
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
            elif choice == "2":
                print("Existing Faculties: ", FACULTIES)
                old_name = input("Enter the Faculty name to rename: ")
                if old_name not in FACULTIES:
                    print("Faculty not found.")
                else:
                    new_name = input("Enter new Faculty name: ")
                    index = FACULTIES.index(old_name)
                    FACULTIES[index] = new_name
                    # Update all students with the old faculty
                    for student in self.students:
                        if student.faculty == old_name:
                            student.faculty = new_name
                    print("Faculty renamed successfully.")
            elif choice == "3":
                print("List of Faculties: ", FACULTIES)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    # New: Function to manage Student Statuses
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
            elif choice == "2":
                print("Existing Statuses: ", STATUSES)
                old_status = input("Enter the Status to rename: ")
                if old_status not in STATUSES:
                    print("Status not found.")
                else:
                    new_status = input("Enter new Status name: ")
                    index = STATUSES.index(old_status)
                    STATUSES[index] = new_status
                    # Update all students with the old status
                    for student in self.students:
                        if student.status == old_status:
                            student.status = new_status
                    print("Status renamed successfully.")
            elif choice == "3":
                print("List of Statuses: ", STATUSES)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    # New: Function to manage Programs
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
            elif choice == "2":
                print("Existing Programs: ", PROGRAMS)
                old_program = input("Enter the Program to rename: ")
                if old_program not in PROGRAMS:
                    print("Program not found.")
                else:
                    new_program = input("Enter new Program name: ")
                    index = PROGRAMS.index(old_program)
                    PROGRAMS[index] = new_program
                    # Update all students with the old program
                    for student in self.students:
                        if student.program == old_program:
                            student.program = new_program
                    print("Program renamed successfully.")
            elif choice == "3":
                print("List of Programs: ", PROGRAMS)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")
