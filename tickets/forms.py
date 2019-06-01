from django.forms import ModelForm
from .models import Ticket
from django import forms

class AddTicketForm(forms.Form):
    TYPE_CHOICES = (
    ('bug', 'Bug'),
    ('feature', 'Feature'),
)

    LABEL_CHOICES = (
    ('functionality', 'Functionality'),
    ('design', 'Design'),
)
    title= forms.CharField(label='Title',required = True)
    type = forms.ChoiceField(label="Type",choices=TYPE_CHOICES,required=True)
    label= forms.ChoiceField(label="Type",choices=LABEL_CHOICES,required=True)
    description = forms.CharField(label='Description', widget = forms.Textarea, required = True)
    image = forms.ImageField(label='Image')