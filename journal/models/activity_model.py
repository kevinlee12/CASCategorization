from django.db import models
from .entry_model import Entry
from localflavor.us import models as localflavor_models


class Activity(models.Model):
    """The Activity model that stores the student activity"""

    name = models.TextField()
    description = models.TextField()
    activity_type = models.CommaSeparatedIntegerField(max_length=3)  # CAS: 123
    learning_obj = models.CommaSeparatedIntegerField(max_length=8)  # 1,...,8
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null=True)
    entries = models.ForeignKey(Entry, on_delete=models.CASCADE)

    # Activity advisor information.
    # This is different from the school advisor, which has a model!
    advisor_name = models.CharField(max_length=30)
    advisor_title = models.CharField(max_length=30)
    advisor_email = models.EmailField()
    advisor_phone = localflavor_models.PhoneNumberField()


    class Meta:
        ordering = ('start_date',)
