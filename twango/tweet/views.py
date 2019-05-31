import re
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View
from twango.notification.models import Notification
from twango.tweet.forms import TwangForm
from twango.tweet.models import Tweet
from twango.twitteruser.models import TwitterUser


# methods for get and post and use view;
class TwangCreationView(View):
    model = Tweet
    form_class = TwangForm
    url_redirect = "home"
    template_name = "../templates/generic.html"
    header = "Twang awayng!"
    button_value = "Post your twang!"

    # if post req; rest is get
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      {"header": self.header, "form": form,
                       "button_value": self.button_value}
                      )

    def post(self, request):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                twang = Tweet.objects.create(
                    user=request.user.twitteruser,
                    twang=data["twang"],
                )
                user_matches = re.findall(r"@(\w+)", data["twang"])
                for match in user_matches:
                    Notification.objects.create(
                        username=TwitterUser.objects.filter(
                            username=match).first(),
                        twang=twang
                    )
            return HttpResponseRedirect(reverse(self.url_redirect))
        return render(request, self.template_name,
                      {"header": self.header,
                       "form": form,
                       "button_value": self.button_value}
                      )


class TwangView(View):
    def get(self, request, id):
        html = "twangs.html"
        twangs = Tweet.objects.filter(id=id)
        return render(request, html, {"twangs": twangs})
