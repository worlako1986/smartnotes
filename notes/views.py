from django.shortcuts import render
from . models import (Notes)

def all_note(request):
    notes = Notes.objects.all()
    return render(request, "notes/all_note.html", {"notes":notes})
