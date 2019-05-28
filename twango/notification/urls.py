from django.urls import path
from twango.notification.views import (notification_view)


urlpatterns = [
    path("notifications/", notification_view),
]
