from django.test import TestCase
from journal.tests.factories import StudentFactory


class StudentTestCase(TestCase):
    """Tests for the Student models"""

    def test_student(self):
        """Test to ensure that Students can be created properly"""
        student = StudentFactory.build()
        self.assertEqual(student.personal_code, '123456')
