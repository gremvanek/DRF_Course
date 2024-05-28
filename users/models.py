from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {"blank": True, "null": True}


class UserRoles(models.TextChoices):
    MEMBER = "member", _("member")
    MODERATOR = "moderator", _("moderator")


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=12, **NULLABLE, verbose_name="телефон")
    city = models.CharField(max_length=100, **NULLABLE, verbose_name="город")
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name="аватарка")
    is_moderator = models.BooleanField(verbose_name="Модератор", **NULLABLE)
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.MEMBER,
        verbose_name="роль",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("pk",)
