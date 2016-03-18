from django.test import TestCase
from journal.models import Student, School


class StudentTestCase(TestCase):
    def setUp(self):
        School.objects.create(
            name='Shaf Academy',
            school_id='0001',
            address='420 7th Street',
            city='San Francisco',
            state='CA',
            country='United States',
        )
    def test_student(self):
        schoo = School.objects.get(school_id='0001')
        student = Student.objects.create(username='wildcassich',
                                         first_name='Wild',
                                         last_name='Cassich',
                                         personal_code='123456',
                                         student_id='4200',
                                         grad_month=5,
                                         grad_year=2016,
                                         student_advisor=None,
                                         student_coordinator=None,
                                         school=schoo)
        self.assertEqual(Student.objects.all()[0], student)
