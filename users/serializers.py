from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import ActivityPeriod


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id','first_name', 'last_name'
        )
        #read_only_fields = ()

class ActivityPeriodSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ActivityPeriod
        fields = '__all__'
        read_only_fields = ('user',)

