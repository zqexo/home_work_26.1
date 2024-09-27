import django_filters

from users.models import Payment


class PaymentFilter(django_filters.FilterSet):
    payment_date = django_filters.DateFilter(
        field_name="payment_date", lookup_expr="exact"
    )
    payment_method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_METHODS)
    amount = django_filters.RangeFilter()

    class Meta:
        model = Payment
        fields = ["payment_date", "payment_method", "amount"]
