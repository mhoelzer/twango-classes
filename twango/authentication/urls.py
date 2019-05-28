# from twango.authentication.models import Author, Recipes
from django.urls import path
from twango.authentication.views import (login_view, logout_view)

# admin.site.register(Author)
# admin.site.register(Recipes)


urlpatterns = [
    path("login/", login_view),
    path("logout/", logout_view)
]
