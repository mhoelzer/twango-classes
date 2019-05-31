from django.urls import path
from twango.tweet.views import (TwangCreationView, TwangView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("twang/", login_required(TwangCreationView.as_view()),
         name="twangcreate"),
    path("twangs/", TwangView),
    path("twang/<int:id>/", TwangView, name="individual")
]
