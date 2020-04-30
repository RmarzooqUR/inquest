from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='login.html'),
        name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
]
