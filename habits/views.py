from rest_framework import generics
from rest_framework.response import Response

from .models import Habit
from .paginators import CustomPagination
from .serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_paginated_response(self, data):
        return Response(data)  # Переопределяем этот метод для отключения пагинации DRF

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Пагинация
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
