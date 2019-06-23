from django.contrib import admin
from .models import Order, OrderLineTicket

# Register your models here.

'''
TabularInline subclass defines the template used to render the Order in the
admin interface. StackedInline is another option
'''
class OrderLineAdminInline(admin.TabularInline):
    model=OrderLineTicket

class OrderAdmin(admin.ModelAdmin):
    '''
    The admin interface has the ability to edit more than one model on a 
    single page. This is known as inlines
    '''
    inlines=(OrderLineAdminInline, )

admin.site.register(Order,OrderAdmin)    
