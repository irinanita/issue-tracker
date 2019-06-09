from django.forms import ModelForm
from .models import Comment
from django import forms

class AddCommentForm(ModelForm):
   class Meta:
       model=Comment
       fields =['content']