from django.contrib import admin
from . import models

# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")


admin.site.register(models.Notes, NotesAdmin)