from django.urls import path
from . import views

from website.views import Home,LoginView,Login_instagram

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login_view/', LoginView.as_view(), name='login_view'),
    path('login_insta/', Login_instagram.as_view(), name='login_insta'),


]