from django.conf.urls import url, include
from .views import registration,user_logout

urlpatterns = [
    url(r'^registration/$',registration,name="registration"),
    url(r'^logout/$', user_logout, name='user_logout'),
]