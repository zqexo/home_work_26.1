from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CoursesConfig
from courses.views import (CourseViewSet, LessonCreateApiView,
                           LessonDestroyApiView, LessonListApiView,
                           LessonRetrieveApiView, LessonUpdateApiView)

app_name = CoursesConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path(
        "lessons/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
] + router.urls
