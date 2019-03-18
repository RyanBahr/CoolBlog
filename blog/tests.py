from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import home

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>The Most Underground Page on the Internet</title>', html)
        self.assertTrue(html.endswith('</html>'))



# Create your tests here.
