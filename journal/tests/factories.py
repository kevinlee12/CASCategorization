import datetime

from factory import SubFactory
from factory.django import DjangoModelFactory
from journal.models import Activity, Entry


class ActivityFactory(DjangoModelFactory):
    """The activity factory"""
    class Meta:
        model = Activity
        django_get_or_create = ('name',)

    name ='Walking the cat'
    description ='Walking the cat around the block'
    activity_type ='1'
    learning_obj ='1,2,3'
    start_date = datetime.date.today
    advisor_name = ''
    advisor_title = ''
    advisor_email = ''
    advisor_phone = ''


class EntryFactory(DjangoModelFactory):
    """The entry factory"""
    class Meta:
        model = Entry
        django_get_or_create = ('activity', 'entry')

    entry = 'I like walking the cat'
    activity = SubFactory(ActivityFactory)
