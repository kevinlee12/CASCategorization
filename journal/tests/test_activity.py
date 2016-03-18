import datetime
import factory

from django.test import SimpleTestCase
from journal.tests.factories import ActivityFactory, EntryFactory


class ActivityTestCase(SimpleTestCase):
    """Sanity checks for activity"""

    def test_activity_serializer(self):
        cat_activity = factory.build(dict, FACTORY_CLASS=ActivityFactory,
                                name='Walking the cat',
                                description='Walking the cat around the block',
                                activity_type='1', learning_obj='1,2,3',
                                start_date=datetime.date.today,
                                advisor_name='Cat',
                                advisor_title='The Great Meow',
                                advisor_email='lion@cat.awe',
                                advisor_phone='737-041-5511')
        self.assertEqual(cat_activity['name'], 'Walking the cat')
        self.assertEqual(cat_activity['description'],
                         'Walking the cat around the block')
        self.assertEqual(cat_activity['advisor_email'],
                         'lion@cat.awe')
        self.assertEqual(cat_activity['advisor_phone'],
                         '737-041-5511')

    def test_no_advisor(self):
        nothing = factory.build(dict, FACTORY_CLASS=ActivityFactory,
                                name='Nothing',
                                description='Nothing',
                                activity_type='1', learning_obj='1',
                                start_date=datetime.date.today)
        self.assertEqual(nothing['name'], 'Nothing')
        self.assertEqual(nothing['advisor_name'], '')
