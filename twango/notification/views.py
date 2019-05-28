from django.shortcuts import render, reverse, HttpResponseRedirect
from twango.notification.forms import NotificationForm
from django.contrib.auth.models import User
from twango.notification.models import Notification
from django.contrib.auth.decorators import login_required
from twango.twitteruser.models import TwitterUser
from twango.tweet.models import Tweet


# maybe in twitteruser, add editable=True in the model
@login_required()
def notification_view(request):
    html = "../templates/notifications.html"
    currentuser = TwitterUser.objects.filter(
        user=request.user).first()
    notifications = Notification.objects.filter(username=currentuser)
    # maybe make it so it deletes once you check and go to this form? no bool?
    for n in notifications:
        n.delete()
    return render(request, html, {"notifications": notifications})

    # button_value = "Signup for your new account, buddy!"
    # if request.method == "POST":
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         user = User.objects.create_user(
    #             username=data["username"], password=data["password"])
    #             # data["username"], data["email"], data["password"])
    #         login(request, user)
    #         TwitterUser.objects.create(
    #             display_name=data["display_name"],
    #             # bio=data["bio"],
    #             user=user
    #         )
    #         return HttpResponseRedirect(reverse("home"))
    # else:
    #     form = SignupForm()
    # return render(request, html, {"form": form})


# def notification_alert_view(request):
#     notification_count = 0
#     currentuser = TwitterUser.objects.filter(
#         username=request.user.twitteruser).first()
#     twangs = Tweet.objects.all()
#     for twang in twangs:
#         if f"@{currentuser}" in twang:
#             notification_count = notification_count + 1
