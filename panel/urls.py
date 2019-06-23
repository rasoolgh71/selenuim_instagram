from django.urls import path
from . import views

from panel.views import panel

urlpatterns = [
    path('home/', panel.as_view(), name='home'),

]