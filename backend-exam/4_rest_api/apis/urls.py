from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1.school import SchoolViewSet
from apis.views.v1.classroom import ClassroomViewSet
from apis.views.v1.teacher import TeacherViewSet
from apis.views.v1.student import StudentViewSet

router = DefaultRouter()
router.register('schools', SchoolViewSet, basename='school')
router.register('classrooms', ClassroomViewSet, basename='classroom')
router.register('teachers', TeacherViewSet, basename='teacher')
router.register('students', StudentViewSet, basename='student')
urlpatterns = [
    path('v1/', include(router.urls))
]
