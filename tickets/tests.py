from django.test import TestCase
from .forms import AddTicketForm


# Create your tests here.


class TestAddTicketForm(TestCase):
    # Imitates a manual DOM manipulation. Trying to pass a value that is not supported
    def test_impossible_to_submit_ticket_with_wrong_type(self):
        form = AddTicketForm(
            {'title': 'Test', 'type': 'some-random-type', 'label': 'design', 'description': 'test', 'image': 'i.png'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['type'],
                         [u'Select a valid choice. some-random-type is not one of the available choices.'])

    def test_impossible_to_submit_ticket_with_wrong_label(self):
        form = AddTicketForm(
            {'title': 'ABC', 'type': 'bug', 'label': 'ux', 'description': 'test', 'image': 'i.png'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['label'], [u'Select a valid choice. ux is not one of the available choices.'])

    # Image is optional so this test is supposed to pass
    def test_submit_ticket_with_no_img(self):
        form = AddTicketForm(
            {'title': 'XYZ', 'type': 'bug', 'label': 'design', 'description': 'test', 'image': ''})
        self.assertTrue(form.is_valid())

    def test_impossible_to_submit_ticket_with_no_title(self):
        form = AddTicketForm(
            {'title': '', 'type': 'bug', 'label': 'design', 'description': 'test', 'image': 'i.png'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
