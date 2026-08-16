วิธีการ test 
cd 4_rest_api
python manage.py runserver

สร้างข้อมูล
http://127.0.0.1:8000/api/v1/schools/
http://127.0.0.1:8000/api/v1/classrooms/
http://127.0.0.1:8000/api/v1/teachers/
http://127.0.0.1:8000/api/v1/students/

หาห้องโดยโรงเรียน
http://127.0.0.1:8000/api/v1/classrooms/?school=1

ข้อมูลห้องเรียน + อัปเดต + ลบ
http://127.0.0.1:8000/api/v1/classrooms/?/
ข้อมูล โรงเรียน + อัปเดต + ลบ
http://127.0.0.1:8000/api/v1/schools/?/

check admin
http://127.0.0.1:8000/admin

superuser:
username a
password a