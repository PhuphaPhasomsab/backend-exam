from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Classroom, Student, Teacher, School
from apis.serializers import ClassroomSerializer, StudentSerializer, TeacherSerializer, SchoolSerializer, ClassroomDetailSerializer, SchoolDetailSerializer
from apis.filters import ClassroomFilter, StudentFilter, TeacherFilter, SchoolFilter
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomSerializer