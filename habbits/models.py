from django.db import models
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    time = models.TimeField()
    action = models.CharField(max_length=100)
    pleasantness = models.BooleanField(default=False, null=True, blank=True)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=100, null=True, blank=True)
    time_required = models.IntegerField(null=True, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f"Привычка пользователя {self.user}: {self.action}, выполняется в {self.place} в {self.time}."
