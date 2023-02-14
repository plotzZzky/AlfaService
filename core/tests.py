from django.test import TestCase

from django.contrib.auth.models import User


class PagesTest(TestCase):
    def setUp(self):
        self.user = {
            'username': 'temporary',
            'password': 'temporary',
        }

        self.test_user = User.objects.create_user(**self.user)

    def test_get_home_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_home_redirect(self):
        response = self.client.get("/", follow=True)
        self.assertRedirects(response, "/users/login/?next=/")

    def test_home_redirect_logged(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_about_status(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
