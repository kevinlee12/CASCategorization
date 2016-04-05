from django.test import Client
from django.test import TestCase

class CategoryTestCase(TestCase):
    def test_cas_category(self):
        """Test to ensure that CAS categories can be rendered properly"""
        c = Client()
        response = c.get('/categories/cas')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['0'], 'Creativity')
        self.assertEqual(response.json()['1'], 'Action')
        self.assertEqual(response.json()['2'], 'Service')

    def test_learning_objectives(self):
        """Test to ensure that learning objectives can be rendered properly"""
        c = Client()
        response = c.get('/categories/learning_objectives')
        self.assertEqual(response.status_code, 200)

        learning_objectives = [
            'Increased awareness of strengths and areas for growth',
            'Undertaking new challenges',
            'Planned and initiated activities',
            'Working collaboratively with others',
            'Showing perseverance and commitment',
            'Engaged with issues of global importance',
            'Consideration of ethical implications',
            'Developing new skills'
        ]
        for ind, _ in enumerate(learning_objectives):
            self.assertEqual(response.json()['{0}'.format(ind)],
                             learning_objectives[ind])

    def test_invalid_category_request(self):
        """Test to ensure that server will throw a 404 if given a bad argument
        """
        c = Client()
        response = c.get('/categories/learning_objectivess')
        self.assertEqual(response.status_code, 404)
