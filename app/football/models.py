from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):

    name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Match(models.Model):
    home_player_one = models.ForeignKey(Player,on_delete=models.CASCADE)
    home_player_two = models.ForeignKey(Player,on_delete=models.CASCADE)
    away_player_one = models.ForeignKey(Player,on_delete=models.CASCADE)
    away_player_two = models.ForeignKey(Player,on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    # positon of players True => player1 is in the front False => player one is in the back
    home_postition = models.BooleanField()
    away_position = models.BooleanField()

    def __str__(self)

    
