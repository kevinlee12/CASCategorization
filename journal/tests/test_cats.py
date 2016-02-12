from django.test import TestCase
from journal.models import Cat

class CatTestCase(TestCase):
    def setUp(self):
        Cat.objects.create(species='Panthera tigris', name='Hobbes')
        Cat.objects.create(species='Felis silvestris', name='Claws')

    def test_cats_attendance(self):
        """Checks if the cats are present"""
        tiger = Cat.objects.get(species='Panthera tigris')
        wildcat = Cat.objects.get(species='Felis silvestris')
        self.assertEqual(tiger.name, 'Hobbes')
        self.assertEqual(wildcat.name, 'Claws')
