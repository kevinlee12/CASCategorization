from django.test import TestCase
from journal.models import Entry


class EntryTestCase(TestCase):
    def setUp(self):
        Entry.objects.create(entry='I like walking the cat')

    def test_entry(self):
        """Checks if the entries were properly created"""
        cat_entry = Entry.objects.get(entry='I like walking the cat')
        self.assertEqual(cat_entry.entry, 'I like walking the cat')
