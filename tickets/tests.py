from django.test import TestCase
from .forms import AddTicketForm
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


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

    # This test is supposed to fail as the uploaded image exceeds the allowed size
    def test_upload_image_too_big(self):
        im = Image.new(mode = 'RGB', size = (3200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)  # seek to the beginning

        image = InMemoryUploadedFile(
            im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None
        )
        file_dict = {'image': image}
        post_dict = {'title': 'Image TEST', 'type': 'bug', 'label': 'design', 'description': 'test'}
        form = AddTicketForm(post_dict, file_dict)
        self.assertFalse(form.is_valid())

    # This test should pass - the uploaded image is valid
    def test_upload_valid_image(self):
        im = Image.new(mode = 'RGB', size = (200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)  # seek to the beginning

        image = InMemoryUploadedFile(
            im_io, None, 'random-name.jpeg', 'image/jpeg', len(im_io.getvalue()), None
        )
        file_dict = {'image': image}
        post_dict = {'title': 'Image TEST', 'type': 'bug', 'label': 'design', 'description': 'test'}
        form = AddTicketForm(post_dict, file_dict)
        self.assertTrue(form.is_valid())