"""twango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from twango.authentication.urls import urlpatterns as authentication_urls
from twango.notification.urls import urlpatterns as notification_urls
from twango.tweet.urls import urlpatterns as tweet_urls
from twango.twitteruser.urls import urlpatterns as twitteruser_urls

from twango.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", HomeView, name="home"),
    path("", login_required(HomeView.as_view()), name="home")
]

urlpatterns += authentication_urls
urlpatterns += notification_urls
urlpatterns += tweet_urls
urlpatterns += twitteruser_urls
