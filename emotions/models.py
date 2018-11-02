from django.db import models
from django.contrib.auth.models import User



class Tweet(models.Model):
    tweet_id = models.CharField(max_length=20)
    original_text = models.CharField(max_length=200)
    #clear_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.original_text

class Vote(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    anger = models.FloatField(default = 0.0)
    disgust = models.FloatField(default = 0.0)
    fear = models.FloatField(default = 0.0)
    joy = models.FloatField(default = 0.0)
    sadness = models.FloatField(default = 0.0)
    surprise = models.FloatField(default = 0.0)
    trust = models.FloatField(default = 0.0)
    anticipation = models.FloatField(default = 0.0)
    



    def __str__(self):
        return str(self.id)
