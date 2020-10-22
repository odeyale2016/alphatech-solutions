from django.db import models
  
class Position(models.Model):
    title= models.CharField(max_length=50)

def __str__(self):
    return self.title 

class Registerdb(models.Model):
    fullname= models.CharField(max_length=120)
    email= models.TextField()
    phone_number= models.TextField()
    company_name= models.TextField()
    message= models.TextField()
    date= models.DateTimeField()
    position=models.ForeignKey(Position, on_delete=models.CASCADE)

 
