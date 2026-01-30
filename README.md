# Hướng dẫn cài đặt (dành cho người clone dự án)

## Yêu cầu môi trường

- Python 3.10+ (khuyến nghị 3.11)
- PostgreSQL 13+ (hoặc tương đương)
- Pip và virtualenv

## Cài đặt nhanh

1. Tạo và kích hoạt môi trường ảo

- Windows (PowerShell):

  python -m venv .venv
  .venv\Scripts\Activate.ps1

2. Cài đặt thư viện

   pip install -r requirement.txt

3. Cấu hình PostgreSQL

Trong [quanlydoan/settings.py](quanlydoan/settings.py), dự án đang dùng cấu hình mặc định:

- Database name: quanlydoan_pg
- User: postgres
- Password: DucPhuc2@
- Host: localhost
- Port: 5432

Bạn cần tạo database tương ứng trước khi chạy migration.

4. Chạy migration

   python manage.py migrate

5. Tạo tài khoản quản trị (tuỳ chọn)

   python manage.py createsuperuser

6. Chạy dự án

   python manage.py runserver

## Ghi chú

- Dự án dùng JWT qua `dj_rest_auth` và `djangorestframework_simplejwt`.
- API schema dùng `drf-spectacular`.

## Mục đích dự án

Dự án tập trung vào quản lý đào tạo và theo dõi đồ án theo nhóm trong môi trường học thuật. Hệ thống định hướng phục vụ hai nhóm người dùng chính: giảng viên và sinh viên.

### Phạm vi chức năng chính

- **Quản lý tài khoản và hồ sơ**: đăng ký, đăng nhập, truy xuất thông tin người dùng; phân vai trò giáo viên/sinh viên.
- **Quản lý môn học & phân công giảng viên**: thiết lập môn học và gán giảng viên phụ trách.
- **Quản lý nhóm đồ án**: tạo nhóm đồ án, gán giảng viên/môn học, quản lý thành viên nhóm.
- **Quản lý nhiệm vụ dự án**: theo dõi các hạng mục công việc (task), người phụ trách và tài liệu tham chiếu.
- **Lịch họp & báo cáo**: tạo lịch họp cho nhóm và cập nhật báo cáo tiến độ sau mỗi buổi.

### Mục tiêu sử dụng

- Chuẩn hoá quy trình theo dõi tiến độ đồ án theo nhóm.
- Tạo kênh tương tác giữa giảng viên và sinh viên thông qua lịch họp/báo cáo.
- Cung cấp API phục vụ web/mobile cho việc quản lý dự án học tập.
