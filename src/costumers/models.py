from django.db import models

# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length=120)
  logo = models.ImageField(upload_to='customers', default='no_picture.jpg')

  #each costumer has to be represnted by just its name eg: Customer.name = "Kandy" it return 'kandy'
  def __str__(self):
    return str(self.name)
