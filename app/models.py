from django.db import models

# Create your models here.



class contact(models.Model):
    
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=120) 
    phone = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name +" ," + " " + self.email

class donation(models.Model):

    name = models.CharField(max_length=20)
    email = models.CharField(max_length=120) 
    phone = models.BigIntegerField()
    pancard  = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name +" ," + " " + self.email
    

        

 

