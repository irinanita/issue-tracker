from django.test import TestCase
from .forms import UserRegistrationForm


# Create your tests here.
class TestUserRegistrationForm(TestCase):
    def test_impossible_to_register_with_only_name(self):
        form = UserRegistrationForm({'username': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_when_passwords_dont_match(self):
        form = UserRegistrationForm({'password1': '123abc', 'password2': '123xyz'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])

    def test_form_valid_when_all_field_requirements_met(self):
        form = UserRegistrationForm(
            {'password1': '123abc', 'password2': '123abc', 'username': 'Test', 'email': 'test@tst.com'})
        self.assertTrue(form.is_valid())
