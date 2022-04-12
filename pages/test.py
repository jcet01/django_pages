# pages/tests.py
from django.test import SimpleTestCase

class PageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contactus_page_status_code(self):
        response = self.client.get('/contactus/')
        self.assertEqual(response.status_code, 200)
