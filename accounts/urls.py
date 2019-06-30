from django.conf.urls import url, include
from .views import registration, user_logout, user_login
from accounts import url_reset

urlpatterns = [
    url(r'^registration/$', registration, name = "registration"),
    url(r'^logout/$', user_logout, name = 'user_logout'),
    url(r'^login/$', user_login, name = 'user_login'),
    url(r'^password-reset/', include(url_reset))
]
