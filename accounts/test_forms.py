from django.test import TestCase
from .forms import UserLoginForm


class TestDjango(TestCase):

    def test_binary(self):
        self.assertEqual(1, 1)


class TestUserLoginForm(TestCase):

    def test_login_form(self):
        form = UserLoginForm({'username': 'username test'})  # instantiates form dict
        self.assertFalse(form.is_valid())
        # self.assertFalse(form.is_valid)

    """
    def test_correct_name_on_form(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        # form is required = standard django validation response
    """