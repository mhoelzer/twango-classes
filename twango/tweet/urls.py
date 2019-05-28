from django.urls import path
# from twango.tweet.views import (twang_creation_view)
from twango.tweet.views import (twang_creation_view, twang_view)


urlpatterns = [
    path("twang/", twang_creation_view),
    path("twangs/", twang_view),
    path("twang/<int:id>/", twang_view, name="individual")
    # make sure str woprks
]
