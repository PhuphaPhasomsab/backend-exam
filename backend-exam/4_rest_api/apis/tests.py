from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apis.models import School, Classroom, Teacher, Student


class SchoolClassroomApiTests(APITestCase):
    def setUp(self):
        self.school = School.objects.create(
            name='โรงเรียนทดสอบ',
            short_name='ทด',
            address='กรุงเทพฯ'
        )
        self.classroom = Classroom.objects.create(
            year=1,
            section='A',
            school=self.school,
        )
        self.teacher = Teacher.objects.create(
            name='สมชาย',
            surname='ใจดี',
            gender='male',
        )
        self.teacher.classroom.add(self.classroom)
        self.student = Student.objects.create(
            name='นัท',
            surname='ทองดี',
            gender='female',
            classroom=self.classroom,
        )

    def test_school_list_endpoint(self):
        url = reverse('school-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_classroom_list_endpoint(self):
        url = reverse('classroom-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teacher_create_endpoint(self):
        url = reverse('teacher-list')
        payload = {
            'name': 'มานะ',
            'surname': 'สวยดี',
            'gender': 'male',
            'classroom': [self.classroom.id],
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'มานะ')

    def test_student_create_endpoint(self):
        url = reverse('student-list')
        payload = {
            'name': 'ปิยวัฒน์',
            'surname': 'พงษ์ดี',
            'gender': 'male',
            'classroom': self.classroom.id,
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'ปิยวัฒน์')
