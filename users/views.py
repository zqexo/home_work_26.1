from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.filters import PaymentFilter
from users.models import Payment, User, Donation
from users.serializers import PaymentSerializer, UserSerializer, DonationSerializer
from users.services import convert_rub_to_dollars, create_stripe_price, create_stripe_session


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
    ordering_fields = ["payment_date", "amount"]
    ordering = ["payment_date"]


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class DonationCreateAPIView(CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def perform_create(self, serializer):
        payment = serializer.save( user=self.request.user)
        amount_in_dollar = convert_rub_to_dollars(payment.amount)
        price = create_stripe_price(amount_in_dollar)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
