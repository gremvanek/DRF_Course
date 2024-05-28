from django.urls import path

from habits.views import HabitListAPIView

app_name = "habits"

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habit-list"),
]
