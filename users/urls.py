from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    path('',
         home, name="home"),
    path('api/users/activities/',
         users_activity, name="users-activity"),
]