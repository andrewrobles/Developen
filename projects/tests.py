
from django.contrib.auth.models import User
from django.test import TestCase

class UserAccountTests(TestCase):
	def test_create_user(self):
		form_data = {'firstname': 'Amani', 'lastname': 'Sidhant', 'username': 'amansidhant', 'password': 'top_secret'}
		self.client.post('/projects/create-account/', form_data)

		user = User.objects.get(username='amansidhant')

		self.assertEqual(user.username, 'amansidhant')
