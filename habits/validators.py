from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_habit(habit):
    # Проверка одновременного выбора связанной привычки и указания вознаграждения
    if habit.related_habit and habit.reward:
        raise ValidationError(
            _(
                "Нельзя одновременно выбирать связанную привычку и указывать вознаграждение."
            )
        )

    # Проверка времени выполнения
    if habit.time_required and habit.time_required > 120:
        raise ValidationError(_("Время выполнения не должно превышать 120 секунд."))

    # Проверка, что связанные привычки могут попадать только привычки с признаком приятной привычки
    if habit.related_habit and not habit.related_habit.pleasantness:
        raise ValidationError(_("Связанная привычка должна быть приятной."))

    # Проверка, что у приятной привычки не может быть вознаграждения или связанной привычки
    if habit.pleasantness:
        if habit.reward:
            raise ValidationError(
                _("У приятной привычки не может быть вознаграждения.")
            )
        if habit.related_habit:
            raise ValidationError(
                _("У приятной привычки не может быть связанной привычки.")
            )

    # Проверка периодичности выполнения привычки
    if habit.frequency < 7:
        raise ValidationError(
            _("Привычка не может выполняться реже, чем 1 раз в 7 дней.")
        )

    # Проверка, что привычка не может не выполняться более 7 дней
    # Мы можем использовать связанные объекты QuerySet для получения связанных записей, если необходимо

    if habit.related_habit:
        # Получаем все связанные привычки
        related_habits = habit.related_habit.all()
        for related_habit in related_habits:
            # Если разница между датой выполнения связанной привычки и текущей датой больше 7 дней,
            # вызываем исключение ValidationError
            if (habit.date - related_habit.date).days > 7:
                raise ValidationError(_("Нельзя не выполнять привычку более 7 дней."))
