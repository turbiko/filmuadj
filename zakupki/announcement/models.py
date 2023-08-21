from string import ascii_letters, digits
from uuid import uuid4

from django.db import models

from .filetools import filename_creation

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    template_document = models.FileField(upload_to=filename_creation, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.title} "
