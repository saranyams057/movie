from django.db import models


# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True,default = None)
    year = models.IntegerField(default = None,blank=True,null=True)
    decs = models.TextField(max_length=250,blank=True,null=True,default = None)
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
