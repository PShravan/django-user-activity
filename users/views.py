from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import *

# Create your views here.

def home(request):
    return redirect('users-activity')

@api_view(['GET',])
def users_activity(request):
    if request.method == 'GET':
        user_queryset = User.objects.prefetch_related('user_activities').all()
        members = []
        for user in user_queryset:
            activity_periods = []
            user_activities = user.user_activities.all()
            for activity in user_activities:
                tz = activity.timezone
                activity_periods.append({"start_time": activity.start_time.strftime("%b %-d %Y  %-I:%M%p"), "end_time": activity.end_time.strftime("%b %-d %Y  %-I:%M%p")})#, "timezone": activity.start_time.tzname()})
            members.append({"id": user.id, "real_name": user.get_full_name(), "tz": tz, "activity_periods":activity_periods})

        return Response({"ok": True, "members": members})
    return Response({"message": "no data found"})

