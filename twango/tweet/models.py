from django.db import models
# from django.contrib.auth.models import User
from twango.twitteruser.models import TwitterUser
from django.utils import timezone


class Tweet(models.Model):
    user = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    # username = models.ForeignKey(
    #     User, on_delete=models.CASCADE)
    # display_name = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    twang = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.username
    #     # return self.user.username
