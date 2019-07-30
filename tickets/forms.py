from django import forms
from .models import Ticket
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


class AddTicketForm(forms.ModelForm):
    def clean_image(self):
        image = self.cleaned_data['image']

        try:
            if image:
                w, h = get_image_dimensions(image)

                # validate dimensions
                max_width = max_height = 1024
                if w > max_width or h > max_height:
                    raise forms.ValidationError(
                        u'Please use an image that is '
                        '%s x %s pixels or smaller.' % (max_width, max_height))

                # validate content type
                main, sub = image.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'png']):
                    raise ValidationError(u'Please use a JPEG or PNG image')

                # validate file size
                if len(image) > (1024 * 1024):
                    raise ValidationError(
                        u'Image file size may not exceed 1MB.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new image
            """
            pass

        return image

    class Meta:
        model = Ticket
        fields = ['title', 'type', 'label', 'description', 'image']
