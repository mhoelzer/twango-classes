from django.contrib import admin
from twango.notification.models import Notification
from twango.tweet.models import Tweet
from twango.twitteruser.models import TwitterUser

admin.site.register(Notification)
admin.site.register(Tweet)
admin.site.register(TwitterUser)