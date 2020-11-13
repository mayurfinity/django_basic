from django.db import models

# Create your models here.
class StudUser(models.Model):
    firstname=models.CharField(max_length=264)
    lastname=models.CharField(max_length=264)
    email=models.EmailField(max_length=254)
    address=models.TextField(max_length=264)
    birthdate=models.DateField()
    phoneno=models.CharField(max_length=20)
    gender=models.CharField(max_length=50)
    file=models.FileField( upload_to='media', max_length=264)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.pk)





