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

## Ảnh Chụp Màn Hình Của Chương Trình

### Giao Diện Chính

![image](https://github.com/user-attachments/assets/e84b5748-31ce-4a11-83bf-0a27cd3e4150)

### Thêm Sinh Viên

![image-1](https://github.com/user-attachments/assets/70c39aa4-1d31-459b-82f3-ce43ff7503ab)

### Xem Tất Cả Sinh Viên

![image-2](https://github.com/user-attachments/assets/2cf7bcf1-8c62-4485-b9ea-c0e2b07d415a)

### Cập Nhật Sinh Viên

![image-3](https://github.com/user-attachments/assets/1c52bb7e-a2bb-4720-9826-e713664cdefa)

### Tìm Kiếm Sinh Viên

![image-4](https://github.com/user-attachments/assets/b041a043-e2db-48b0-ae24-5bc98991eae4)

### Xóa Sinh Viên

![image-5](https://github.com/user-attachments/assets/1b2b5b2d-b76f-4fac-8b1f-74cdfda97df2)

### Thoát Chương Trình

![image-6](https://github.com/user-attachments/assets/3548c2b8-6ab5-4041-b4f2-8ca690bc7614)



# Hệ Thống Quản Lý Sinh Viên

## Phiên Bản 2.0

Version 2.0 đã bổ sung các tính năng mới sau:

- **Import/Export Dữ Liệu:** Hỗ trợ nhập (import) và xuất (export) dữ liệu sinh viên theo 2 định dạng CSV và JSON.
- **Logging Mechanism:** Ghi lại các hoạt động (thêm, cập nhật, xóa, import/export,…) vào file `app.log` nhằm phục vụ troubleshooting và audit.
- **Hiển Thị Version & Build Date:** Cho phép xem phiên bản ứng dụng và ngày build (tính động dựa trên thời gian sửa đổi của file `main.py`).
- **Quản Lý Danh Mục Nâng Cao:** Quản lý, thêm mới và đổi tên các danh mục: Khoa, Tình trạng sinh viên, Chương trình đào tạo.
- **Tìm Kiếm Nâng Cao:** Hỗ trợ tìm kiếm sinh viên theo khoa, và kết hợp tìm kiếm theo khoa & tên sinh viên.

## Cấu Trúc Mã Nguồn

Chương trình được chia thành các file sau:

1. **`student.py`**:

   - Chứa class `Student` để lưu trữ thông tin sinh viên.
   - Các hàm validation để kiểm tra tính hợp lệ của dữ liệu nhập vào (email, số điện thoại, ngày sinh, năm học, giới tính, khoa, tình trạng sinh viên).

2. **`student_manager.py`**:

   - Chứa class `StudentManager` để quản lý danh sách sinh viên.
   - Cung cấp các phương thức để thêm, xóa, cập nhật, tìm kiếm, quản lý danh mục (Khoa, Tình trạng, Chương trình), import/export CSV & JSON và logging.

3. **`main.py`**:
   - Chứa chương trình chính để chạy ứng dụng.
   - Cung cấp giao diện dòng lệnh (CLI) với menu các chức năng, bao gồm hiển thị version & build date.
   - Cấu hình logging để ghi lại các hoạt động của ứng dụng.

## Yêu Cầu Hệ Thống

- Python 3.x đã được cài đặt trên máy tính.

## Hướng Dẫn Cài Đặt và Chạy Chương Trình

### Bước 1: Tải Mã Nguồn

- Sau khi tải file mã nguồn, hãy giải nén file để có thư mục chứa các file mã nguồn.

### Bước 2: Chạy Chương Trình

- Mở terminal hoặc command prompt và di chuyển đến thư mục chứa mã nguồn.
- Chạy chương trình bằng lệnh:
  ```bash
  python main.py
  ```

### Bước 3: Sử Dụng Chương Trình

Khi chương trình chạy, bạn sẽ thấy một menu với các tùy chọn:

1. **Add a new student:** Nhập thông tin sinh viên.
2. **Delete a student:** Xóa sinh viên dựa trên MSSV.
3. **Update a student:** Cập nhật thông tin dựa trên MSSV.
4. **Search for a student:** Tìm kiếm sinh viên theo MSSV/Name, theo Khoa hoặc theo kết hợp Khoa & Tên.
5. **List all students:** Hiển thị tất cả sinh viên.
6. **Export data to CSV:** Xuất dữ liệu sinh viên ra file CSV.
7. **Import data from CSV:** Nhập dữ liệu từ file CSV.
8. **Export data to JSON:** Xuất dữ liệu sinh viên ra file JSON.
9. **Import data from JSON:** Nhập dữ liệu từ file JSON.
10. **Manage Faculties:** Quản lý danh mục Khoa.
11. **Manage Student Statuses:** Quản lý danh mục Tình trạng sinh viên.
12. **Manage Programs:** Quản lý danh mục Chương trình đào tạo.
13. **Show Version and Build Date:** Hiển thị thông tin version và ngày build của ứng dụng.
14. **Exit:** Kết thúc chương trình.

## Hướng Dẫn Sử Dụng Các Tính Năng Mới

### 1. Import/Export Dữ Liệu

- **Export CSV/JSON:** Chọn các mục 6 hoặc 8 trong menu để xuất dữ liệu ra file `students.csv` hoặc `students.json`.
- **Import CSV/JSON:** Chọn các mục 7 hoặc 9 để nhập dữ liệu từ file tương ứng.  
  _Lưu ý: Khi import, danh sách sinh viên hiện tại sẽ được làm mới (clear) để tránh trùng lặp._

### 2. Logging Mechanism

- Mọi thao tác (thêm, xóa, cập nhật, tìm kiếm, import/export,…) được ghi vào file `app.log`.  
  Bạn có thể kiểm tra file này để audit và troubleshoot các vấn đề trong production.

### 3. Hiển Thị Version & Build Date

- Chọn mục 13 trong menu để hiển thị phiên bản ứng dụng và ngày build.  
  Ngày build được tính dựa trên thời gian sửa đổi của file `main.py`, đảm bảo luôn đúng theo phiên bản cập nhật mới nhất.

## Ảnh Chụp Màn Hình Minh Chứng

### Giao Diện Chính

![image](https://github.com/user-attachments/assets/17a1c1f8-d54f-47ac-b38e-cfbdde0c70a8)

### Lưu trữ dữ liệu

![image](https://github.com/user-attachments/assets/4e110dea-1611-42a1-8bc1-00e95f004a3e)

### Cho phép đổi tên & thêm mới

![image](https://github.com/user-attachments/assets/1ebe409b-4f87-48ba-a2b1-144ecfb91c68)
![image](https://github.com/user-attachments/assets/af282238-92c1-4ad4-8a07-58fbcaf52379)

### Tìm Kiếm Sinh Viên (Tìm theo Khoa & Kết hợp Khoa + Tên)

![image](https://github.com/user-attachments/assets/9717ee4f-f32f-4b6c-98a9-b6d77952ad3d)

### Import/Export Dữ Liệu CSV & JSON

![image](https://github.com/user-attachments/assets/054b2ce3-2e24-4bb2-b05d-54b0bd5f8981)
![image](https://github.com/user-attachments/assets/542d5666-d1b6-47c4-8cab-b3c76c327385)
![image](https://github.com/user-attachments/assets/4e110dea-1611-42a1-8bc1-00e95f004a3e)

### Logging Mechanism

![image](https://github.com/user-attachments/assets/b3c9dfe5-58d5-4a3b-becc-d580c19248df)

### Hiển Thị Version & Build Date

![image](https://github.com/user-attachments/assets/cea01ff2-2efc-4b51-809a-8a77f4339ad9)

## Kiểm Tra Tính Hợp Lệ Của Dữ Liệu

Chương trình sẽ tự động kiểm tra tính hợp lệ của các trường dữ liệu như:

- **Email:** Định dạng email hợp lệ (ví dụ: `example@domain.com`).
- **Số điện thoại:** Phải là 10 chữ số.
- **Ngày sinh:** Định dạng `YYYY-MM-DD`.
- **Năm học:** Phải là một năm hợp lệ (từ 1900 đến năm hiện tại).
- **Giới tính:** Chỉ chấp nhận các giá trị `Nam`, `Nữ`, hoặc `Khác`.
- **Khoa:** Chỉ chấp nhận các khoa được định nghĩa sẵn.
- **Tình trạng sinh viên:** Chỉ chấp nhận các tình trạng được định nghĩa sẵn.

## Ứng Dụng Logging và Audit

- Các hoạt động của người dùng sẽ được ghi vào file `app.log` với thông tin thời gian, mức độ log và mô tả thao tác.  
  Điều này giúp theo dõi hoạt động của ứng dụng trong môi trường production và hỗ trợ troubleshooting khi có vấn đề xảy ra.
