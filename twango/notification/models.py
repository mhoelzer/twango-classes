from django.db import models
from twango.twitteruser.models import TwitterUser
from twango.tweet.models import Tweet


class Notification(models.Model):
    # wassign to someone; post message with your username (tweet about them)
    # and get info from that; how to see that the not was seen
    username = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    twang = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    was_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"@{self.username.username} twanged: {self.twang.twang}"
        # self.notiftwang.tweettwang
