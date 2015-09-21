from django.db import models
from django.contrib.auth.models import User

from website.random_primary import RandomPrimaryIdModel

class AmI(models.Model):
    owner = models.ForeignKey(User, primary_key=True)
    seen = models.BooleanField(default=False)
    am_i = models.BooleanField(default=False)
