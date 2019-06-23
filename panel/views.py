from django.shortcuts import render
from django.views.generic.base import View,TemplateView,HttpResponse
# Create your views here.


class panel(TemplateView):
    template_name = 'panel/index_base.html'
