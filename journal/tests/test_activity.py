import datetime
import factory

from django.test import SimpleTestCase
from django.test import TransactionTestCase
from journal.tests.factories import ActivityFactory
from journal.models import Activity


class ActivityTestCase(SimpleTestCase):
    """Sanity checks for activity"""

    def test_activity_full_field(self):
        """Tests to ensure that the model can be populated fully"""
        cat_activity = factory.build(dict, FACTORY_CLASS=ActivityFactory,
                                     name='Walking the cat',
                                     description='Walking the cat around '
                                                 'the block',
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
        """Tests that the advisor field can be left blank."""
        nothing = factory.build(dict, FACTORY_CLASS=ActivityFactory,
                                name='Nothing',
                                description='Nothing',
                                activity_type='1', learning_obj='1',
                                start_date=datetime.date.today)
        self.assertEqual(nothing['name'], 'Nothing')
        self.assertEqual(nothing['advisor_name'], '')

class ActivityDBTestCase(TransactionTestCase):
    """Tests to ensure that the DB behaves as expected"""

    def test_id_is_uuid(self):
        """Tests that the UUID of Activity is not """
        activity = Activity.objects.create(name='Walking the cat',
                                           description='Walking the cat around '
                                                       'the block',
                                           activity_type='1',
                                           learning_obj='1,2,3',
                                           start_date=datetime.date.today,
                                           advisor_name='Cat',
                                           advisor_title='The Great Meow',
                                           advisor_email='lion@cat.awe',
                                           advisor_phone='737-041-5511')
        self.assertNotEqual(activity.id, 1)
