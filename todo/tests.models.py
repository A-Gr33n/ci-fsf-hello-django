from django.test import TestCase 
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.object.create(name='Test Todo Item')
        self assertfalse(item.done)

    def test_item_string_method_returns_ name(self):
        item = Item.object.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
