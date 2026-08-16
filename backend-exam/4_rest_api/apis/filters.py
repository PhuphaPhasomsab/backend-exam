from django_filters import FilterSet, filters
from .models import Classroom, Student, Teacher, School

# code here
# หา classroom จาก 'school','year','section'
class ClassroomFilter(FilterSet):

    class Meta:
        model = Classroom
        fields = ['school']
        # หาโรงเรียนจาก 'school'
class SchoolFilter(FilterSet):

    class Meta:
        model = School
        fields = ['name']
        # หาจารจาก 'classroom','school','gender','name','surname'
class TeacherFilter(FilterSet):
    school = filters.CharFilter(field_name='classroom__school__name', lookup_expr='icontains')
    class Meta:
        model = Teacher
        fields = ['classroom','school','gender','name','surname']
        # หานักเรียนจาก 'classroom','school','gender','name','surname'
class StudentFilter(FilterSet):
    school = filters.CharFilter(field_name='classroom__school__name', lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ['classroom','school','gender','name','surname']
