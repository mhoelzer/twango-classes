from django.urls import path
from twango.twitteruser.views import (
    signup_view, profile_view, following_or_not_view)

urlpatterns = [
    path("signup/", signup_view),
    path("followstatus/<slug:username>/", following_or_not_view),
    # slugs specifically look for url stuff; when had it as str, it was also
    # looking for the favicon.ico; could see this with a breakpoint and vars()
    # this should go above the strr b/c otherwise it thinks it's a string
    # specifics go first
    path("<slug:username>/", profile_view),
]
