import datetime

from django.test import TestCase
from journal.tests.factories import ActivityFactory, EntryFactory
from journal.models import Entry

class EntryTestCase(TestCase):
    def setUp(self):
        cat_a = ActivityFactory.create(name='Walking the cat',
                              description='Walking the cat around the block',
                              activity_type='1', learning_obj='1,2,3',
                              start_date=datetime.date.today,
                              advisor_name='Cat',
                              advisor_title='The Great Meow',
                              advisor_email='lion@cat.awe',
                              advisor_phone='737-041-5511')
        EntryFactory.create(entry='I like walking the cat', activity=cat_a)

    def test_entry(self):
        """Checks if the entries were properly created"""
        cat_entry = Entry.objects.get(entry='I like walking the cat')
        self.assertEqual(cat_entry.entry, 'I like walking the cat')
