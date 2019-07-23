from django.conf.urls import url
from .views import checkout, checkout_buy_app, thank_you

urlpatterns = [
    url(r'^$', checkout, name = 'checkout'),
    url(r'^buy-app$', checkout_buy_app, name = 'checkout-app'),
    url(r'^thank-you$', thank_you, name = 'thank-you'),
]
