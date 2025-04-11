from django.db import models

class student(models.Model):
    
    name = models.CharField(max_length=100, null =False, blank = False)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    qualifications = models.TextField(null =True, blank = False)



class product(models.Model):
    product_name = models.CharField(max_length= 200, null =False, blank = False)
    price = models.IntegerField()
    description = models.TextField()
    reviews = models.TextField()
    ratings = models.IntegerField()
    
    




    
    
    

    
        
    
class Meta:     
    abstract = True