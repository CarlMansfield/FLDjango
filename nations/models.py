from django.db import models


class Nation(models.Model):
    country = models.CharField(max_length=50, primary_key=True)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.country


class League(models.Model):
    lName = models.CharField(max_length=50)
    teams = models.IntegerField()
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def __str__(self):
        return self.lName


class Team(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    played = models.IntegerField()
    image_url = models.CharField(max_length=2083)
