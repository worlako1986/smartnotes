from django.urls import path
from . import views

app_name = "notes"
urlpatterns  = [
    path("notes", views.AllNoteView.as_view(), name= "all_note" ),
    path("notes/<int:pk>", views.NoteDetailView.as_view(), name= "detail")
]