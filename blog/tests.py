from django.test import TestCase
from blog.views import home_page
from django.urls import resolve
from django.http import HttpRequest
from blog.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Cool Blog</title>', html)
        self.assertTrue(html.endswith('</html>'))



# Create your tests here.
