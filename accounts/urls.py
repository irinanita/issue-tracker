from django.conf.urls import url
from .views import registration,user_logout,user_login

urlpatterns = [
    url(r'^registration/$',registration,name="registration"),
    url(r'^logout/$', user_logout, name='user_logout'),
    url(r'^login/$', user_login, name='user_login')
]