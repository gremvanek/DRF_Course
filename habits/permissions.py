from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Проверка прав доступа: только владелец привычки может редактировать или удалять ее.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS запросы
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить доступ только владельцу привычки
        return obj.user == request.user


class ReadOnlyUnlessPublic(permissions.BasePermission):
    """
    Проверка прав доступа: разрешить только чтение публичных привычек.
    """

    def has_permission(self, request, view):
        # Разрешить доступ к привычкам только для чтения (GET, HEAD, OPTIONS)
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        # Разрешить доступ только к публичным привычкам для чтения
        return obj.public
