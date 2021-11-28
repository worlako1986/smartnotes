from django.urls import path
from . import views

app_name = "notes"
urlpatterns  = [
    path("notes", views.all_note, name= "all_note" )
]