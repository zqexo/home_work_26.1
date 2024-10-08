import json

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson, Subscription
from courses.validators import validate_forbidden_words, validate_video_link


class LessonSerializer(ModelSerializer):
    title = serializers.CharField(validators=[validate_forbidden_words])
    materials = serializers.ListField(
        child=serializers.URLField(validators=[validate_video_link]),
        allow_empty=True,
        read_only=True,
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_forbidden_words])
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

    @staticmethod
    def get_lessons(course):
        lessons = Lesson.objects.filter(course=course.pk)
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField(read_only=True)
    lessons = SerializerMethodField(read_only=True)

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


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "course"]
