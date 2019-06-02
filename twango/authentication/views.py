from django.shortcuts import render, HttpResponseRedirect
from twango.authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic.edit import FormView


class LoginView(FormView):
    template_name = "../templates/generic.html"
    form_class = LoginForm
    url_redirect = "/"
    header = "Login"
    button_value = "Login, buddy!"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      {"header": self.header, "form": form,
                       "button_value": self.button_value}
                      )

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(
            username=data["username"], password=data["password"])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(
                self.request.GET.get("next", self.url_redirect))
        return render(self.request, self.template_name,
                      {"header": self.header, "form": form,
                       "button_value": self.button_value}
                      )


class LogoutView(View):
    def get(self, request):
        html = "logout.html"
        logout(request)
        return render(request, html)
