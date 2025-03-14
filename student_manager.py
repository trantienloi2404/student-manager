import csv
import os
import json
import logging
from datetime import datetime, timedelta
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

ALLOWED_EMAIL_DOMAIN = "@student.hcmus.edu.vn"
ALLOWED_STATUS_TRANSITIONS = {
    "Đang học": {"Đang học", "Bảo lưu", "Tốt nghiệp", "Đình chỉ"},
    "Đã tốt nghiệp": {"Đã tốt nghiệp"},
}


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_from_csv()
        self.deletion_restriction_enabled = True
        self.deletion_window_minutes = 30
        logging.info(
            "StudentManager initialized. Deletion restriction: %s, window: %d minutes",
            self.deletion_restriction_enabled,
            self.deletion_window_minutes,
        )

    def add_student(self):
        print("Add a new student:")
        mssv = input("MSSV: ")
        # Business Rule 01: Kiểm tra MSSV duy nhất
        for s in self.students:
            if s.mssv == mssv:
                print("Error: MSSV đã tồn tại. Vui lòng nhập MSSV khác.")
                return

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
        while not (validate_email(email) and email.endswith(ALLOWED_EMAIL_DOMAIN)):
            print(f"Invalid email. Email phải có đuôi {ALLOWED_EMAIL_DOMAIN}.")
            email = input("Email: ")
        phone = input("Phone: ")
        while not validate_phone(phone):
            print(
                "Invalid phone number. Please enter a valid phone number (e.g., +84XXXXXXXXX or 0[3|5|7|8|9]XXXXXXXX)."
            )
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
        self.save_to_csv()

    def delete_student(self):
        mssv = input("Enter MSSV to delete: ")
        for student in self.students:
            if student.mssv == mssv:
                # Check deletion restriction if enabled
                if self.deletion_restriction_enabled:
                    now = datetime.now()
                    allowed_time = student.creation_time + timedelta(
                        minutes=self.deletion_window_minutes
                    )
                    print("Now: ",now)
                    print("allow: ",allowed_time)
                    if now > allowed_time:
                        print(
                            "Cannot delete student. Deletion allowed only within",
                            self.deletion_window_minutes,
                            "minutes of creation.",
                        )
                        logging.warning(
                            "Deletion restriction: Attempt to delete student MSSV=%s after allowed window",
                            mssv,
                        )
                        return
                self.students.remove(student)
                print("Student deleted successfully!")
                logging.info("Deleted student with MSSV=%s", mssv)
                self.save_to_csv()  # Auto-save after deletion
                return
        print("Student not found.")
        logging.warning("Attempted to delete non-existent student with MSSV=%s", mssv)

    def update_student(self):
        mssv = input("Enter MSSV to update: ")
        for student in self.students:
            if student.mssv == mssv:
                print("Update student information:")
                # (Giả sử MSSV không được cập nhật)
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
                while not (
                    validate_email(email) and email.endswith(ALLOWED_EMAIL_DOMAIN)
                ):
                    print(f"Invalid email. Email phải có đuôi {ALLOWED_EMAIL_DOMAIN}.")
                    email = input(f"Email ({student.email}): ") or student.email
                student.email = email
                phone = input(f"Phone ({student.phone}): ") or student.phone
                while not validate_phone(phone):
                    print("Invalid phone number. Please enter a valid phone number.")
                    phone = input(f"Phone ({student.phone}): ") or student.phone
                student.phone = phone

                # Business Rule 04: Kiểm tra chuyển đổi tình trạng
                current_status = student.status
                new_status = input(f"Status ({student.status}): ") or student.status
                if new_status not in ALLOWED_STATUS_TRANSITIONS.get(
                    current_status, {current_status}
                ):
                    print(
                        f"Transition from '{current_status}' to '{new_status}' is not allowed."
                    )
                    logging.warning(
                        "Invalid status transition: %s -> %s",
                        current_status,
                        new_status,
                    )
                    return
                student.status = new_status

                print("Student updated successfully!")
                logging.info("Updated student: MSSV=%s", mssv)
                self.save_to_csv()
                return
        print("Student not found.")
        logging.warning("Attempted to update non-existent student with MSSV=%s", mssv)

    # Updated search functions remain similar (omitted here for brevity)

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
            results = [
                student
                for student in self.students
                if (
                    search_term.lower() in student.mssv.lower()
                    or search_term.lower() in student.name.lower()
                )
            ]
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

    # New: Delete Faculty/Status/Program if no student uses them
    def delete_faculty(self):
        faculty = input("Enter the Faculty to delete: ")
        if faculty not in FACULTIES:
            print("Faculty does not exist.")
            return
        # Check if any student uses this faculty
        for student in self.students:
            if student.faculty == faculty:
                print("Cannot delete Faculty. It is assigned to one or more students.")
                return
        FACULTIES.remove(faculty)
        print("Faculty deleted successfully.")
        logging.info("Deleted Faculty: %s", faculty)

    def delete_status(self):
        status = input("Enter the Student Status to delete: ")
        if status not in STATUSES:
            print("Status does not exist.")
            return
        for student in self.students:
            if student.status == status:
                print("Cannot delete Status. It is assigned to one or more students.")
                return
        STATUSES.remove(status)
        print("Status deleted successfully.")
        logging.info("Deleted Student Status: %s", status)

    def delete_program(self):
        program = input("Enter the Program to delete: ")
        if program not in PROGRAMS:
            print("Program does not exist.")
            return
        for student in self.students:
            if student.program == program:
                print("Cannot delete Program. It is assigned to one or more students.")
                return
        PROGRAMS.remove(program)
        print("Program deleted successfully.")
        logging.info("Deleted Program: %s", program)

    # New: Export confirmation letter in HTML and Markdown formats
    def export_confirmation_letter(self):
        mssv = input("Enter MSSV of the student to export confirmation letter: ")
        student = None
        for s in self.students:
            if s.mssv == mssv:
                student = s
                break
        if not student:
            print("Student not found.")
            return

        print("Choose format: 1. HTML  2. Markdown")
        fmt_choice = input("Enter your choice: ")
        if fmt_choice == "1":
            self._export_letter_html(student)
        elif fmt_choice == "2":
            self._export_letter_md(student)
        else:
            print("Invalid format selection.")

    def _export_letter_html(self, student):
        # Template for HTML confirmation letter
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Giấy Xác Nhận Tình Trạng Sinh Viên</title>
  <style>
    body {{ font-family: Arial, sans-serif; }}
    .header {{ text-align: center; }}
    .content {{ margin: 20px; }}
    hr {{ border: 1px solid #000; }}
  </style>
</head>
<body>
  <div class="header">
    <h1>TRƯỜNG ĐẠI HỌC Khoa Học Tự Nhiên</h1>
    <h2>PHÒNG ĐÀO TẠO</h2>
    <p>📍 Địa chỉ: 227 Nguyễn Văn Cừ Quận 5 Thành Phố Hồ Chí Minh | 📞 Điện thoại: [Số điện thoại] | 📧 Email: [Email liên hệ]</p>
    <hr>
  </div>
  <div class="content">
    <h2>GIẤY XÁC NHẬN TÌNH TRẠNG SINH VIÊN</h2>
    <p>Trường Đại học Khoa Học Tự Nhiên xác nhận:</p>
    <h3>1. Thông tin sinh viên:</h3>
    <ul>
      <li><strong>Họ và tên:</strong> {student.name}</li>
      <li><strong>Mã số sinh viên:</strong> {student.mssv}</li>
      <li><strong>Ngày sinh:</strong> {student.dob}</li>
      <li><strong>Giới tính:</strong> {student.gender}</li>
      <li><strong>Khoa:</strong> {student.faculty}</li>
      <li><strong>Chương trình đào tạo:</strong> {student.program}</li>
      <li><strong>Khóa:</strong> [KXX - Năm nhập học]</li>
    </ul>
    <h3>2. Tình trạng sinh viên hiện tại:</h3>
    <ul>
      <li>Đang theo học</li>
      <li>Đã hoàn thành chương trình, chờ xét tốt nghiệp</li>
      <li>Đã tốt nghiệp</li>
      <li>Bảo lưu</li>
      <li>Đình chỉ học tập</li>
      <li>Tình trạng khác</li>
    </ul>
    <h3>3. Mục đích xác nhận:</h3>
    <ul>
      <li>Xác nhận đang học để vay vốn ngân hàng</li>
      <li>Xác nhận làm thủ tục tạm hoãn nghĩa vụ quân sự</li>
      <li>Xác nhận làm hồ sơ xin việc / thực tập</li>
      <li>Xác nhận lý do khác: [Ghi rõ]</li>
    </ul>
    <h3>4. Thời gian cấp giấy:</h3>
    <p>Giấy xác nhận có hiệu lực đến ngày: [DD/MM/YYYY]</p>
    <p>📍 <strong>Xác nhận của Trường Đại học Khoa Học Tự Nhiên</strong></p>
    <p>📅 Ngày cấp: [DD/MM/YYYY]</p>
    <p>🖋 <strong>Trưởng Phòng Đào Tạo</strong> (Ký, ghi rõ họ tên, đóng dấu)</p>
  </div>
  <hr>
</body>
</html>
"""
        filename = f"confirmation_{student.mssv}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_template)
        print(f"Confirmation letter exported to {filename}.")
        logging.info(
            "Exported confirmation letter in HTML for student MSSV=%s", student.mssv
        )

    def _export_letter_md(self, student):
        # Template for Markdown confirmation letter
        md_template = f"""
# TRƯỜNG ĐẠI HỌC Khoa Học Tự Nhiên  
**PHÒNG ĐÀO TẠO**  
📍 Địa chỉ: 227 Nguyễn Văn Cừ Quận 5 Thành Phố Hồ Chí Minh  
📞 Điện thoại: [Số điện thoại] | 📧 Email: [Email liên hệ]  

---  

## GIẤY XÁC NHẬN TÌNH TRẠNG SINH VIÊN

Trường Đại học Khoa Học Tự Nhiên xác nhận:

### 1. Thông tin sinh viên:
- **Họ và tên:** {student.name}
- **Mã số sinh viên:** {student.mssv}
- **Ngày sinh:** {student.dob}
- **Giới tính:** {student.gender}
- **Khoa:** {student.faculty}
- **Chương trình đào tạo:** {student.program}
- **Khóa:** [KXX - Năm nhập học]

### 2. Tình trạng sinh viên hiện tại:
- Đang theo học
- Đã hoàn thành chương trình, chờ xét tốt nghiệp
- Đã tốt nghiệp
- Bảo lưu
- Đình chỉ học tập
- Tình trạng khác

### 3. Mục đích xác nhận:
- Xác nhận đang học để vay vốn ngân hàng
- Xác nhận làm thủ tục tạm hoãn nghĩa vụ quân sự
- Xác nhận làm hồ sơ xin việc / thực tập
- Xác nhận lý do khác: [Ghi rõ]

### 4. Thời gian cấp giấy:
- Giấy xác nhận có hiệu lực đến ngày: [DD/MM/YYYY]

📍 **Xác nhận của Trường Đại học Khoa Học Tự Nhiên**  

📅 Ngày cấp: [DD/MM/YYYY]  

🖋 **Trưởng Phòng Đào Tạo**  
(Ký, ghi rõ họ tên, đóng dấu)

---
"""
        filename = f"confirmation_{student.mssv}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(md_template)
        print(f"Confirmation letter exported to {filename}.")
        logging.info(
            "Exported confirmation letter in Markdown for student MSSV=%s", student.mssv
        )

    # Existing management functions for Faculties, Statuses, and Programs are updated below:
    def manage_faculties(self):
        while True:
            print("\nManage Faculties")
            print("1. Add new Faculty")
            print("2. Rename existing Faculty")
            print("3. Delete Faculty")
            print("4. List Faculties")
            print("5. Back to main menu")
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
                self.delete_faculty()
            elif choice == "4":
                print("List of Faculties: ", FACULTIES)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def manage_statuses(self):
        while True:
            print("\nManage Student Statuses")
            print("1. Add new Status")
            print("2. Rename existing Status")
            print("3. Delete Status")
            print("4. List Statuses")
            print("5. Back to main menu")
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
                self.delete_status()
            elif choice == "4":
                print("List of Statuses: ", STATUSES)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def manage_programs(self):
        while True:
            print("\nManage Programs")
            print("1. Add new Program")
            print("2. Rename existing Program")
            print("3. Delete Program")
            print("4. List Programs")
            print("5. Back to main menu")
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
                self.delete_program()
            elif choice == "4":
                print("List of Programs: ", PROGRAMS)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")
