from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply pending changes to makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=40)
    messageBox = models.TextField()
    def __str__(self):
        return self.name

class Register(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    def __str__(self):
        return self.firstName

class Custom(models.Model):
    customFlowerName = models.CharField(max_length = 100)
    customSizeOfBouquet = models.CharField(max_length=10)
    customBouquetPicture = models.FileField()
    def __str__(self):
        return self.customFlowerName