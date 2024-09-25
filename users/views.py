from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializers import PaymentSerializer



class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
