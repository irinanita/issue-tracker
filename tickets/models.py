from django.db import models
from django.conf import settings
from django.utils import timezone

class Ticket(models.Model):
    '''
    A single Ticket
    '''
    TYPE_CHOICES = (
    ('bug', 'Bug'),
    ('feature', 'Feature'),
)

    LABEL_CHOICES = (
    ('functionality', 'Functionality'),
    ('design', 'Design'),
)
    
    STATUS_CHOICES = (
    ('opened', 'Opened'),
    ('closed', 'Closed'),
)
    
    title = models.CharField(max_length=60)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    description = models.TextField()
    type=  models.CharField(max_length=7, choices=TYPE_CHOICES)
    label= models.CharField(max_length=13, choices=LABEL_CHOICES)
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default="opened",null=True)
    creation_date = models.DateTimeField(auto_now_add=True) 
    #auto_now and auto_now_add imply the field is not user-editable and must always get set to this value
    score = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img",blank="True",null="True")
    #img correspond to our img direcotry under media
    
    def __str__(self):
        return "{0} -- Type: {1} -- Status: {2} ".format(self.title, self.type, self.status)
