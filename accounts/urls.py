from django.conf.urls import url, include
from .views import registration, user_logout, user_login, user_profile, delete_avatar
from accounts import url_reset

urlpatterns = [
    url(r'^registration/$', registration, name = "registration"),
    url(r'^logout/$', user_logout, name = 'user_logout'),
    url(r'^login/$', user_login, name = 'user_login'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^myprofile/$', user_profile, name = 'user_profile'),
    url(r'^delete-avatar/$', delete_avatar, name = 'delete_avatar')
]
