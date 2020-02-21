from django.db import models
from django.contrib.auth.models import User

class WorkDiary(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.IntegerField()