from django.db import models

from habits.validators import validate_habit
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель привычки"
    )
    place = models.CharField(
        max_length=100, verbose_name="Место, где необходимо выполнять привычку"
    )
    time = models.TimeField(verbose_name="Время, когда необходимо выполнять привычку.")
    action = models.CharField(
        max_length=100, verbose_name="Действие, которое представляет собой привычка."
    )
    pleasantness = models.BooleanField(
        default=False,
        **NULLABLE,
        verbose_name="Привычка, которую можно привязать к "
        "выполнению полезной привычки.",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="привычка, которая связана с другой привычкой, "
        "важно указывать для полезных привычек, но не для приятных",
    )
    frequency = models.PositiveIntegerField(
        default=1,
        verbose_name="периодичность выполнения " "привычки для напоминания в днях.",
    )
    reward = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name="чем пользователь должен себя " "вознаградить после выполнения.",
    )
    time_required = models.IntegerField(
        **NULLABLE,
        verbose_name="время, которое предположительно "
        "потратит пользователь на выполнение привычки.",
    )
    public = models.BooleanField(
        default=False,
        verbose_name="привычки можно публиковать в общий доступ, "
        "чтобы другие пользователи могли брать в "
        "пример чужие привычки.",
    )

    def __str__(self):
        return f"Привычка пользователя {self.user}: {self.action}, выполняется в {self.place} в {self.time}."

    def clean(self):
        validate_habit(self)
