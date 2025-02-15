# Hệ Thống Quản Lý Sinh Viên

## Cấu Trúc Mã Nguồn

Chương trình được chia thành các file sau:

1. **`student.py`**:

   - Chứa class `Student` để lưu trữ thông tin sinh viên.
   - Các hàm validation để kiểm tra tính hợp lệ của dữ liệu nhập vào (email, số điện thoại, ngày sinh, năm học, giới tính, khoa, tình trạng sinh viên).

2. **`student_manager.py`**:

   - Chứa class `StudentManager` để quản lý danh sách sinh viên.
   - Cung cấp các phương thức để thêm, xóa, cập nhật, tìm kiếm và hiển thị sinh viên.

3. **`main.py`**:
   - Chứa chương trình chính để chạy ứng dụng.
   - Cung cấp giao diện dòng lệnh (CLI) để người dùng tương tác với hệ thống.

## Yêu Cầu Hệ Thống

- Python 3.x đã được cài đặt trên máy tính.

## Hướng Dẫn Cài Đặt và Chạy Chương Trình

### Bước 1: Tải Mã Nguồn

- Sau khi tải thư mục 22127240.zip về máy thì hãy giải nén file 22127240.zip ta được một thư mục 22127240 chứa các file như phần cấu trúc mã nguồn.

### Bước 2: Chạy Chương Trình

- Mở terminal hoặc command prompt và di chuyển đến thư mục chứa mã nguồn.
- Chạy chương trình bằng lệnh:
  ```bash
  python main.py
  ```

### Bước 3: Sử Dụng Chương Trình

- Khi chương trình chạy, bạn sẽ thấy một menu với các tùy chọn sau:

  1. **Add a new student**: Nhập thông tin sinh viên.
  2. **Delete a student**: Xóa sinh viên dựa trên MSSV.
  3. **Update a student**: Cập nhật thông tin dựa trên MSSV.
  4. **Search for a student**: Tìm kiếm theo MSSV hoặc tên.
  5. **List all students**: Hiển thị tất cả sinh viên trong hệ thống.
  6. **Exit**: Kết thúc chương trình.

- Làm theo hướng dẫn trên màn hình để thực hiện các thao tác.

## Kiểm Tra Tính Hợp Lệ Của Dữ Liệu

Chương trình sẽ tự động kiểm tra tính hợp lệ của các trường dữ liệu như:

- **Email**: Định dạng email hợp lệ (ví dụ: `example@domain.com`).
- **Số điện thoại**: Phải là 10 chữ số.
- **Ngày sinh**: Định dạng `YYYY-MM-DD`.
- **Năm học**: Phải là một năm hợp lệ (từ 1900 đến năm hiện tại).
- **Giới tính**: Chỉ chấp nhận các giá trị `Nam`, `Nữ`, hoặc `Khác`.
- **Khoa**: Chỉ chấp nhận các khoa được định nghĩa sẵn.
- **Tình trạng sinh viên**: Chỉ chấp nhận các tình trạng được định nghĩa sẵn.
