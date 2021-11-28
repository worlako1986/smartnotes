from django.db import models
import datetime

# Create your models here.

class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 200, null= False)
    content  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notes"


    def __json__(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "content": self.content
        }
