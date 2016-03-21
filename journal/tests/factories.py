import datetime

from factory import SubFactory
from factory.django import DjangoModelFactory
from journal.models import Activity, Entry
from journal.models import School
from journal.models import Coordinator, Student


class ActivityFactory(DjangoModelFactory):
    """The Activity Factory"""
    class Meta:
        model = Activity
        django_get_or_create = ('name',)

    name = 'Walking the cat'
    description = 'Walking the cat around the block'
    activity_type = '1'
    learning_obj = '1,2,3'
    start_date = datetime.date.today
    advisor_name = ''
    advisor_title = ''
    advisor_email = ''
    advisor_phone = ''


class EntryFactory(DjangoModelFactory):
    """The Entry Factory"""
    class Meta:
        model = Entry
        django_get_or_create = ('activity', 'entry')

    entry = 'I like walking the cat'
    activity = SubFactory(ActivityFactory)


class SchoolFactory(DjangoModelFactory):
    """The School Factory"""
    class Meta:
        model = School
        django_get_or_create = ('name')

    name = 'Shaf Academy'
    school_id = '0001'
    address = '420 7th Street'
    city = 'San Francisco'
    state = 'CA'
    country = 'United States'


class CoordinatorFactory(DjangoModelFactory):
    """The Coordinator Factory"""
    class Meta:
        model = Coordinator
        django_get_or_create = ('name')

    school = SubFactory(SchoolFactory)
    username = 'lionking'
    first_name = 'Lion'
    last_name = 'Prowler'
    email = 'lion@savanna.wild'

class StudentFactory(DjangoModelFactory):
    """The Student Factory"""
    class Meta:
        model = Student
        django_get_or_create = ('name', 'personal_code')

    username = 'wildcassich'
    first_name = 'Wild'
    last_name = 'Cassich'
    personal_code = '123456'
    student_id = '4200'
    grad_month = 5
    grad_year = 2016
    student_coordinator = SubFactory(CoordinatorFactory)
    school = SubFactory(SchoolFactory)
