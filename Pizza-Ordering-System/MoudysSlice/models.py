from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.conf import settings
from django.utils import timezone
from views import *

class AccountManager(BaseUserManager):
    def create_user(self, user, email, password=None, **extra_fields):
        if not user:
            raise ValueError("The Username must be set")
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(user=user, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user, email, password=None, **extra_fields):

        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(user, email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    user = models.CharField(verbose_name="username", max_length=20, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "user"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.user

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Topping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExtraTopping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name


class Pizza(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', null=True)
    order_time = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, null=True)
    Pepperoni = models.BooleanField(default=False) 
    Chicken = models.BooleanField(default=False)
    Ham = models.BooleanField(default=False) 
    Pineapple = models.BooleanField(default=False)
    Peppers = models.BooleanField(default=False)
    Mushrooms = models.BooleanField(default=False)
    Onions = models.BooleanField(default=False)
    Sausages = models.BooleanField(default=False)
    Jalapeños = models.BooleanField(default=False)
    Pesto = models.BooleanField(default=False)


def validate_card_expiry_date(value):
    try:
        expiry_date = datetime.strptime(value, "%m/%y")
        if expiry_date < datetime.now():
            raise ValidationError('The card expiry date is in the past. Please update your card.')
    except ValueError:
        raise ValidationError('Enter a valid expiry date in MM/YY format.')

class OrderDelivery(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='delivery', null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    card = models.CharField(max_length=16, validators=[RegexValidator(r'^\d{16}$', message='Enter a valid 16-digit card number.')])
    expirydate = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(r'^(0[1-9]|1[0-2])\/\d{2}$', message='Enter a valid expiry date in MM/YY format.'),
            validate_card_expiry_date,
        ]
    )
    cvv = models.CharField(max_length=3, validators=[RegexValidator(r'^\d{3}$', message='Enter a valid 3-digit CVV.')])
