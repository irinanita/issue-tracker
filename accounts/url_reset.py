from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
# download all the views that are provided by Django by default
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name = 'password_reset'),
    url(r'^done/$', password_reset_done, name = "password_reset_done"),
    # creating a unique URL for each password reset
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name = "password_reset_confirm"),
    url(r'^complete/$', password_reset_complete, name = "password_reset_complete"),
]
