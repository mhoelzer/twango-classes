from django.urls import path
from twango.tweet.views import (twang_creation_view, twang_view)
# from twango.tweet.views import (TwangCreationView, twang_view)
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("twang/", twang_creation_view),
    # path("twang/", login_required(TwangCreationView.as_view()), name="twangcreate"),
    path("twangs/", twang_view),
    path("twang/<int:id>/", twang_view, name="individual")
]
