from django.contrib import admin
from .models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    fields=['title','type','status','score','description','label']
    readonly_fields = ['user','score','description','title']
admin.site.register(Ticket, TicketAdmin)


  