from unittest import TestCase
from Yandexapi_test import folder_creation

class TestYaApi(TestCase):
    def test_folder_creation(self):
        response = folder_creation()
        expected = '201'
        self.assertEqual(folder_creation, expected)
