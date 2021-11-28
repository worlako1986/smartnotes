from django.shortcuts import render
from django.http import Http404
from django.views.generic.detail import DetailView
from . models import (Notes)
from django.views.generic import (ListView, DetailView)


class AllNoteView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/all_note.html"



class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/note_detail.html"

    