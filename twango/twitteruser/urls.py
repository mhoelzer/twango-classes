from django.urls import path
from twango.twitteruser.views import (
    signup_view, profile_view, following_or_not_view)

urlpatterns = [
    path("signup/", signup_view),
    path("followstatus/<str:username>/", following_or_not_view),
    # this should go above the strr b/c otherwise it thinks it's a string
    # specifics go first
    path("<str:username>/", profile_view),
]
