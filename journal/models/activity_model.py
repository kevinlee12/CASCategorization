from django.db import models
from .entry_model import Entry


class Activity(models.Model):
    """The Activity model that stores the student activity"""

    name = models.TextField()
    description = models.TextField()
    activity_type = models.CharField(max_length=3)  # CAS
    learning_obj = models.CharField(max_length=8)  # 12345678
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null=True)
    entries = models.ForeignKey(Entry, on_delete=models.CASCADE)

    class Meta:
        ordering = ('start_date',)
