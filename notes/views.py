from django.shortcuts import render
from django.http import Http404
from . models import (Notes)

def all_note(request):
    notes = Notes.objects.all()
    return render(request, "notes/all_note.html", {"notes":notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk = pk)
    except Exception as e:
        raise Http404
    else:
        return render(request, "notes/note_detail.html", {"note": note})
