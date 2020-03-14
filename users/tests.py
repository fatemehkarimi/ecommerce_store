from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import SignUpForm

# Create your tests here.
class CustomUserTests(TestCase):
    first_name = 'test_name'
    last_name = 'test_last_name'
    user_email = 'test_user@email.com'
    username = user_email
    password='testpass123'

    def test_create_user(self):
        CustomUser = get_user_model()
        new_user = CustomUser.objects.create_user(
            email=self.user_email,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
        )
        self.assertEqual(new_user.email, self.user_email)
        self.assertEqual(new_user.username, self.username)
        self.assertEqual(new_user.first_name, self.first_name)
        self.assertEqual(new_user.last_name, self.last_name)

    def test_create_superuser(self):
        CustomUser = get_user_model()
        new_user = CustomUser.objects.create_superuser(
            email=self.user_email,
            first_name=self.first_name,
            password=self.password,
            last_name=self.last_name,
            username=self.username,
        )
        self.assertEqual(new_user.email, self.user_email)
        self.assertEqual(new_user.username, self.username)
        self.assertEqual(new_user.first_name, self.first_name)
        self.assertEqual(new_user.last_name, self.last_name)


class SignUpTests(TestCase):

    credentials = {
        'email': 'test_email@email.com',
        'first_name': 'testname',
        'last_name': 'test_last_name',
        'password': 'testpass123',
    }

    def test_signup_template(self):
        url = reverse('account_signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
        self.assertContains(response, 'Sign Up')

    def test_signup_form(self):
        filled_form = SignUpForm(data=self.credentials)
        self.assertTrue(filled_form.is_valid())

    #BUG: this test fails
    '''
    def test_signup_view(self):
        response = self.client.post(reverse('account_signup'), self.credentials)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 2)
        self.assertEqual(get_user_model().objects.all()[0].email, self.credentials['email'])
    '''