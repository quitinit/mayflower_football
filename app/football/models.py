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
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.user.email}"

class Team(models.Model):
    name = models.CharField(max_length=255)
    player_one = models.OneToOneField(Player,related_name='%(class)s_player_one', on_delete=models.CASCADE)
    player_two = models.OneToOneField(Player,related_name='%(class)s_player_two', on_delete=models.CASCADE)
    home_postition = models.BooleanField()

    def __str__(self):
        return f"{self.player_one.user} -- {self.player_two.user}"
class Match(models.Model):
    
    home_team = models.OneToOneField(Team,related_name='%(class)s_home_team',on_delete=models.CASCADE)
    away_team = models.OneToOneField(Team,related_name='%(class)s_away_team',on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    # positon of players True => player1 is in the front False => player one is in the back

    def __str__(self):
        return f"{self.home_team} VS {self.away_team}"
class BestMode(models.TextChoices):
    ONE_MODE = "1"
    BEST_OF_THREE_MODE = "3"
    BEST_OF_FIVE_MODE = "5"

class Game(models.Model):
    
    
    
    matches = models.ManyToManyField(Match)
    time = models.DateTimeField()
    mode = models.CharField(max_length=1,
                  choices=BestMode.choices,
                  default=BestMode.ONE_MODE)    
