from django.db import models

class Contact(models.Model):
    full_name= models.CharField(max_length=200)
    subject= models.TextField()
    email= models.TextField()
    phone_number= models.TextField()
    company_name= models.TextField()
    message= models.TextField()
    date= models.DateTimeField()

def __str__(self):
    return self.email 
