from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET',])
def users_activity(request):
    if request.method == 'GET':
        user_queryset = User.objects.all()
        members = []
        for user in user_queryset:
            activity_periods = []
            user_activities =  ActivityPeriod.objects.filter(user=user)
            for activity in user_activities:
                tz = activity.timezone
                activity_periods.append({"start_time": activity.start_time.strftime("%b %-d %Y  %-H:%M%p"), "end_time": activity.end_time.strftime("%b %-d %Y  %-H:%M%p")})#, "timezone": activity.start_time.tzname()})
            members.append({"id": user.id, "real_name": user.get_full_name(), "tz": tz, "activity_periods":activity_periods})

        return Response({"ok": True, "members": members})
    return Response({"message": "no data found"})