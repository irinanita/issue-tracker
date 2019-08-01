from django.conf.urls import url
from .views import view_cart, delete_product

urlpatterns = [
    url(r'^$', view_cart, name = 'view_cart'),
    url(r'^delete/(?P<pk>\d+)', delete_product, name = "delete_product"),
]
