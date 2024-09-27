from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payment/", PaymentViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
