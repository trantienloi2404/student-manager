# HỆ THỐNG QUẢN LÝ SINH VIÊN – VERSION 3.0

## Các Tính Năng Chính
 
## Ex03

1. **MSSV phải là duy nhất**  
   - Khi thêm hoặc cập nhật sinh viên, hệ thống phải kiểm tra và từ chối nếu có sinh viên khác có cùng MSSV.

2. **Email phải thuộc một tên miền nhất định và có thể cấu hình động**  
   - Ví dụ: Hệ thống chỉ chấp nhận email có đuôi `@student.hcmus.edu.vn`.

3. **Số điện thoại phải có định dạng hợp lệ theo quốc gia (configurable)**  
   - Ví dụ: Với Việt Nam, số điện thoại phải theo định dạng `+84XXXXXXXXX` hoặc `0[3|5|7|8|9]XXXXXXXX`.

4. **Tình trạng sinh viên chỉ có thể thay đổi theo quy tắc định sẵn (configurable)**  
   - Ví dụ:
     - `"Đang học"` có thể chuyển sang `"Bảo lưu"`, `"Tốt nghiệp"`, hoặc `"Đình chỉ"`.
     - `"Đã tốt nghiệp"` không thể chuyển lại thành `"Đang học"`.

---

## Ex04

5. **Quy tắc xóa sinh viên**  
   - Chỉ cho phép xóa sinh viên nếu thời gian từ lúc tạo (creation date/time) chưa vượt quá khoảng thời gian cấu hình (ví dụ: 30 phút).

6. **Bật/Tắt quy tắc business**  
   - Người dùng có thể bật hoặc tắt việc áp dụng các quy tắc trên.

7. **Hiển thị logo/tên trường**  
   - Tất cả các màn hình giao diện của ứng dụng phải hiển thị logo hoặc tên trường.

8. **Xóa danh mục**  
   - Cho phép xóa các danh mục như Khoa, Tình trạng sinh viên và Chương trình đào tạo nếu không có dữ liệu sinh viên liên kết.

9. **Xuất giấy xác nhận tình trạng sinh viên**  
    - Hệ thống phải hỗ trợ xuất giấy xác nhận ra ít nhất 2 định dạng (ví dụ: HTML và Markdown) với mẫu sau:

    ---
    
    **TRƯỜNG ĐẠI HỌC Khoa Học Tự Nhiên**  
    **PHÒNG ĐÀO TẠO**  
    📍 Địa chỉ: 227 Nguyễn Văn Cừ Quận 5 Thành Phố Hồ Chí Minh  
    📞 Điện thoại: [Số điện thoại] | 📧 Email: [Email liên hệ]  
    
    ---  
    
    ### **GIẤY XÁC NHẬN TÌNH TRẠNG SINH VIÊN**  
    
    Trường Đại học Khoa Học Tự Nhiên xác nhận:  
    
    **1. Thông tin sinh viên:**  
    - **Họ và tên:** [Họ và tên sinh viên]  
    - **Mã số sinh viên:** [MSSV]  
    - **Ngày sinh:** [DD/MM/YYYY]  
    - **Giới tính:** [Nam/Nữ/Khác]  
    - **Khoa:** [Tên khoa]  
    - **Chương trình đào tạo:** [Cử nhân/Kỹ sư/Thạc sĩ...]  
    - **Khóa:** [KXX - Năm nhập học]  
    
    **2. Tình trạng sinh viên hiện tại:**  
    - Đang theo học  
    - Đã hoàn thành chương trình, chờ xét tốt nghiệp  
    - Đã tốt nghiệp  
    - Bảo lưu  
    - Đình chỉ học tập  
    - Tình trạng khác  
    
    **3. Mục đích xác nhận:**  
    - Xác nhận đang học để vay vốn ngân hàng  
    - Xác nhận làm thủ tục tạm hoãn nghĩa vụ quân sự  
    - Xác nhận làm hồ sơ xin việc / thực tập  
    - Xác nhận lý do khác: [Ghi rõ]  
    
    **4. Thời gian cấp giấy:**  
    - Giấy xác nhận có hiệu lực đến ngày: [DD/MM/YYYY]  
    
    📍 **Xác nhận của Trường Đại Học Khoa Học Tự Nhiên**  
    
    📅 Ngày cấp: [DD/MM/YYYY]  
    
    🖋 **Trưởng Phòng Đào Tạo**  
    (Ký, ghi rõ họ tên, đóng dấu)  
    
    ---

## Hình ảnh minh chứng
