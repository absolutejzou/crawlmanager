from django.db import models
from django.utils.timezone import now
from crawlmanager.apps.foundation.choices import Sex, UserStatus


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    sex = models.SmallIntegerField(choices=Sex.choices)
    status = models.SmallIntegerField(choices=UserStatus.choices)
    created_at = models.DateTimeField(default=now)
