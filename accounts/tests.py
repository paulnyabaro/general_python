from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPateTest(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get('/accounts/signup')
        self.assertEqual(response.status_code, 200)