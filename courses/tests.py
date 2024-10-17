from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="testuser@example.com")
        self.course = Course.objects.create(
            title="test", description="test description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="test", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)
        self.moderator_group = Group.objects.create(name="moders")

    def test_course_retrieve(self):
        """Тестирование редактирования курса"""
        url = reverse("courses:course-detail", kwargs={"pk": self.course.pk})
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "test")

    def test_course_list_access(self):
        url = reverse("courses:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_moderator_course_create_access(self):
        url = reverse("courses:course-list")
        self.moderator_group.user_set.add(self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_course_delete(self):
        url = reverse("courses:course-detail", kwargs={"pk": self.course.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
