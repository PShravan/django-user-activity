import os, random, pytz
from faker import Faker

import django
from django.core.management.base import BaseCommand, CommandError
from users.models import *
from django.contrib.auth.models import User

django.setup()


fake = Faker()

timezones_list = pytz.common_timezones

def populate_user():
    print("\npopulating 100 users...")
    for _ in range(100):
        user,created = User.objects.get_or_create(username=fake.user_name())
        if created:
            user.first_name=fake.first_name()
            user.last_name=fake.last_name()
            user.username=fake.user_name()
            user.email=fake.email()
            user.set_password(fake.password())
            user.is_active=True
            user.save()
    print("Done")

def populate_activity_period():
    print("\npopulating user activity...")
    user_ids=User.objects.values_list('id',flat=True)
    for _ in range(1000):
        try:
            user = User.objects.get(id=random.choice(user_ids))
        except User.DoesNotExist:
            continue
        
        timezone = random.choice(timezones_list)
        tz = pytz.timezone(timezone)
        starttime = fake.date_time(tzinfo=tz)
        ActivityPeriod.objects.create(
            user=user,
            start_time=starttime,
            end_time=fake.date_time_between(start_date=starttime, tzinfo=tz),
            timezone = timezone
        )
    print("Done")


class Command(BaseCommand):
    help = "loads the dummy data into the models"

    def add_arguments(self, parser):
        pass
        # parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        print("\npopulating dummy date in database...")
        print("\ndeleting all previous data...")
        User.objects.all().delete()
        ActivityPeriod.objects.all().delete()
        print("Done")
        populate_user()
        populate_activity_period()