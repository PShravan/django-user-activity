from django.db import models
from django.conf import settings
# Create your models here.

class ActivityPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, related_name='user_activities')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    timezone = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.timezone