from django.forms import ModelForm
from .models import Ticket

class AddTicketForm(ModelForm):
   class Meta:
       model=Ticket
       fields =['title','type','label','description','image']
       