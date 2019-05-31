from django.shortcuts import render, reverse, HttpResponseRedirect
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from django.contrib.auth.decorators import login_required
from twango.tweet.models import Tweet
from twango.twitteruser.models import TwitterUser
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
# dispatch allows the requests to run; it's from the method
class HomeView(View):
    def get(self, request):
        html = "home.html"
        currentuser = TwitterUser.objects.get(
            user=request.user)
        twangs_of_user = Tweet.objects.filter(user=request.user.twitteruser)
        followers = currentuser.following.all()
        twangs_of_followings = Tweet.objects.filter(user__in=followers)
        twangs = (twangs_of_followings |
                twangs_of_user).distinct().order_by("-date")
        return render(request, html, {"twangs": twangs})
