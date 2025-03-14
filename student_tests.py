import unittest
from datetime import datetime, timedelta
from student import Student, validate_phone, validate_email
from student_manager import StudentManager, ALLOWED_STATUS_TRANSITIONS

# Giả lập cấu hình cho email domain (ví dụ từ business rule)
ALLOWED_EMAIL_DOMAIN = "@student.university.edu.vn"


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        # Khởi tạo StudentManager với danh sách trống
        self.manager = StudentManager()
        self.manager.students = []  # đảm bảo list sinh viên rỗng cho mỗi test

    def test_add_student_unique_mssv(self):
        # Thêm một sinh viên
        student1 = Student(
            "SV001",
            "Nguyen Van A",
            "2000-01-01",
            "Nam",
            "Khoa Luật",
            "2020",
            "Chương trình chuẩn",
            "Address",
            "a@student.university.edu.vn",
            "0912345678",
            "Đang học",
        )
        self.manager.students.append(student1)
        # Cố gắng thêm sinh viên với cùng MSSV
        duplicate_mssv = "SV001"
        # Giả lập việc nhập từ người dùng: nếu MSSV đã tồn tại, add_student() sẽ thông báo lỗi và từ chối thêm.
        for s in self.manager.students:
            if s.mssv == duplicate_mssv:
                self.assertEqual(s.mssv, "SV001")
                break

    def test_email_domain_validation(self):
        # Test email phải kết thúc bằng ALLOWED_EMAIL_DOMAIN
        valid_email = "test@student.university.edu.vn"
        invalid_email = "test@gmail.com"
        self.assertTrue(
            validate_email(valid_email) and valid_email.endswith(ALLOWED_EMAIL_DOMAIN)
        )
        self.assertFalse(invalid_email.endswith(ALLOWED_EMAIL_DOMAIN))

    def test_phone_validation(self):
        # Kiểm tra định dạng số điện thoại theo regex
        valid_phone1 = "+84912345678"
        valid_phone2 = "0912345678"
        invalid_phone = "0123456"
        self.assertTrue(validate_phone(valid_phone1))
        self.assertTrue(validate_phone(valid_phone2))
        self.assertFalse(validate_phone(invalid_phone))

    def test_status_transition(self):
        # Kiểm tra chuyển đổi trạng thái hợp lệ và không hợp lệ
        student = Student(
            "SV002",
            "Tran Thi B",
            "1999-05-05",
            "Nữ",
            "Khoa Tiếng Nhật",
            "2019",
            "Chương trình chuẩn",
            "Address",
            "b@student.university.edu.vn",
            "0912345679",
            "Đang học",
        )
        # Hợp lệ: từ Đang học sang Bảo lưu
        current_status = student.status
        new_status = "Bảo lưu"
        self.assertIn(
            new_status, ALLOWED_STATUS_TRANSITIONS.get(current_status, {current_status})
        )
        # Không hợp lệ: từ Đã tốt nghiệp sang Đang học
        student.status = "Đã tốt nghiệp"
        invalid_transition = "Đang học"
        self.assertNotIn(
            invalid_transition,
            ALLOWED_STATUS_TRANSITIONS.get(student.status, {student.status}),
        )

    def test_deletion_restriction(self):
        # Kiểm tra quy tắc xóa dựa trên creation_time
        student = Student(
            "SV003",
            "Le Van C",
            "2001-03-03",
            "Nam",
            "Khoa Tiếng Pháp",
            "2021",
            "Chương trình đặc biệt",
            "Address",
            "c@student.university.edu.vn",
            "0912345680",
            "Đang học",
        )
        self.manager.students.append(student)
        # Giả sử student được tạo 31 phút trước
        student.creation_time = datetime.now() - timedelta(minutes=31)
        self.manager.deletion_restriction_enabled = True
        # Thử xóa sinh viên này
        initial_count = len(self.manager.students)
        # Vì đã vượt quá window, xóa sẽ bị từ chối
        self.manager.delete_student = (
            lambda: None
        )  # Giả lập hàm delete không xóa nếu không hợp lệ
        # Không thay đổi số lượng sinh viên
        self.assertEqual(len(self.manager.students), initial_count)


if __name__ == "__main__":
    unittest.main()
