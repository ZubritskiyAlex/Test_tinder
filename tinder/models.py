from __future__ import unicode_literals
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

SEX_ENUM = (
    (1, 'Man',),
    (2, 'Woman',)
)
SUBSCRIPTION_ENUM = (
    (1, 'Basic'),
    (2, 'VIP'),
    (3, 'Premium')
)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
            return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.IntegerField(choices=SEX_ENUM)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(99)],
        verbose_name="Age",
        default=18
    )
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Description", blank=True, null=True)
    # images = models.ImageField(verbose_name='Photo')
    subscription = models.IntegerField(choices=SUBSCRIPTION_ENUM, verbose_name='Kind of subscription')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
