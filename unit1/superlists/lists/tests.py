from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def setUp(self):
        print("HomePageTest setUp")

    def tearDown(self):
        print("HomePageTest tearDown")

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
