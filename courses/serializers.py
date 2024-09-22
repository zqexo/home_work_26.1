import json

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    @staticmethod
    def get_lessons(course):
        lessons = Lesson.objects.filter(course=course.pk)
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    @staticmethod
    def get_lessons_count(course):
        return Lesson.objects.filter(course=course.pk).count()

    @staticmethod
    def get_lessons(course):
        lessons = Lesson.objects.filter(course=course.pk)
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = ("title", "description", "lessons_count", "lessons")
