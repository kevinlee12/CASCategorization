from django.test import TestCase
from journal.models import Student


class StudentTestCase(TestCase):
    def test_student(self):
        student = Student.objects.create(username='wildcassich',
                                         first_name='Wild',
                                         last_name='Cassich',
                                         personal_code='123456',
                                         student_id='4200',
                                         grad_month=5,
                                         grad_year=2016,
                                         student_advisor=None,
                                         student_coordinator=None)
        self.assertEqual(Student.objects.all()[0], student)
