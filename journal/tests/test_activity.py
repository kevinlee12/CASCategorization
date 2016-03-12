import datetime

from django.test import TestCase
from journal.models import Activity, Entry
from journal.serializers import ActivitySerializer


class ActivityTestCase(TestCase):
    """Sanity checks for activity"""
    def setUp(self):
        cat_e = Entry.objects.create(entry='I like walking the cat')
        Activity.objects.create(name='Walking the cat',
                                description='Walking the cat around the block',
                                activity_type='1', learning_obj='1,2,3',
                                entries=cat_e,
                                start_date=datetime.date.today)

    def test_activity_serializer(self):
        cat_activity = Activity.objects.get(name='Walking the cat')
        self.assertEqual(cat_activity.name, 'Walking the cat')

        cat_serializer = ActivitySerializer(cat_activity)
        self.assertEqual(cat_serializer.data['description'],
                         'Walking the cat around the block')
