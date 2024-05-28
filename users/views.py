from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            # Разрешаем создание пользователя без аутентификации
            return []
        # Для остальных действий требуем аутентификацию
        return [IsAuthenticated()]
