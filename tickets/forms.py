from django.forms import ModelForm
from .models import Ticket
from django import forms

class AddTicketForm(ModelForm):
   class Meta:
       model=Ticket
       fields =['title','type','label','description','image']
       
    # title= forms.CharField(label='Title',required = True)
    # type = forms.ChoiceField(label="Type",choices=TYPE_CHOICES,required=True)
    # label= forms.ChoiceField(label="Type",choices=LABEL_CHOICES,required=True)
    # description = forms.CharField(label='Description', widget = forms.Textarea, required = True)
    # image = forms.ImageField(label='Image',required=False)