from django.urls import path

from habits.views import HabitListAPIView


urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habit-list"),
]
