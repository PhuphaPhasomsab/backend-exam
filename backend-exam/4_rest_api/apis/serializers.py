from rest_framework import serializers
from .models import Classroom, Student, Teacher, School


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'year', 'section', 'school']


class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'gender', 'classroom']


class TeacherSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(many=True, queryset=Classroom.objects.all())

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'surname', 'gender', 'classroom']

    def create(self, validated_data):
        classroom_data = validated_data.pop('classroom', [])
        teacher = Teacher.objects.create(**validated_data)
        teacher.classroom.set(classroom_data)
        return teacher

    def update(self, instance, validated_data):
        classroom_data = validated_data.pop('classroom', None)
        instance = super().update(instance, validated_data)
        if classroom_data is not None:
            instance.classroom.set(classroom_data)
        return instance


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'short_name', 'address']


class ClassroomDetailSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    teachers = TeacherSerializer(many=True, read_only=True)
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'year', 'section', 'school', 'students', 'teachers']


class SchoolDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'short_name', 'address', 'classroom_count', 'teacher_count', 'student_count', 'classrooms']

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classroom__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).distinct().count()