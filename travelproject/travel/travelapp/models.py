from django.db import models


# Create your models here.
class places(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    decs = models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    team_name = models.CharField(max_length=250)
    team_image = models.ImageField(upload_to='pics2')
    team_desc = models.TextField()

    def __str__(self):
        return self.team_name
