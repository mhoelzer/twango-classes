# from twango.authentication.models import Author, Recipes
from django.urls import path
from twango.authentication.views import (login_view, LogoutView)

# admin.site.register(Author)
# admin.site.register(Recipes)


urlpatterns = [
    path("login/", login_view),
    path("logout/", LogoutView.as_view())
]
