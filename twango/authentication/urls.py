# from twango.authentication.models import Author, Recipes
from django.urls import path
from twango.authentication.views import (login_view, LogoutView)
# from twango.authentication.views import (LoginView, LogoutView)

# admin.site.register(Author)
# admin.site.register(Recipes)


urlpatterns = [
    path("login/", login_view),
    # path("login/", LoginView.as_view(), name="log_me_mcfriggin_in"),
    path("logout/", LogoutView.as_view())
]
