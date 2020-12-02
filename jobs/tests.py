from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class HomePageTests(TestCase):
	def test_home_page(self):
		response=self.client.get('/')
		self.assertEqual(response.status_code,404)
	def test_home_page_url_name(self):
		response=self.client.get(reverse('all_post'))
		self.assertEqual(response.status_code,404)
