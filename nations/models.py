from django.db import models

class Nation(models.Model):
    country = models.CharField(max_length=50)
    image_url = models.CharField(max_length=2083)

class Team(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    played = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class League(models.Model):
    lName = models.CharField(max_length=50)
    teams = models.IntegerField()
    image_url = models.CharField(max_length=2083, null=True)
