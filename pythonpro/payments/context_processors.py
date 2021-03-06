from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'SUBSCRIPTIONS_OPEN': settings.SUBSCRIPTIONS_OPEN,
        'PAGSEGURO_PAYMENT_PLAN': settings.PAGSEGURO_PAYMENT_PLAN,
    }
