from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.datetime.today()}    
