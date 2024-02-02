from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from common.models import TimestampModel, StatefulModel, UUIDModel
from users.managers import AuthenticableManager, UserManager

class Authenticable(AbstractBaseUser, TimestampModel, StatefulModel, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    objects = AuthenticableManager()

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return hasattr(self, 'admin')

    @property
    def is_company(self):
        return hasattr(self, 'company')

class User(TimestampModel, UUIDModel):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Relations
    authenticable = models.OneToOneField('users.Authenticable', on_delete=models.PROTECT)

    objects = UserManager()

    def __str__(self) -> str:
        return f'[{self.authenticable.email}] {self.name} {self.last_name}'
    
class Profile(TimestampModel):
    description =  models.TextField(max_length=500)
    country = models.CharField(max_length=2)
    phone = models.CharField(max_length=30)
    image =  models.ImageField()
    curriculum = models.FileField()

    # Relations
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'[{self.user.authenticable.email}] {self.user.name} {self.user.last_name}'


class Admin(TimestampModel):
    ip = models.CharField(max_length=50)

    # Relations
    authenticable = models.OneToOneField('users.Authenticable', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'[{self.authenticable.email}] {self.ip}'


class Company(UUIDModel, TimestampModel, StatefulModel):
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=50)

    # Relations
    authenticable = models.OneToOneField('users.Authenticable', on_delete=models.PROTECT)

    def __str__(self):
        return f'[{self.authenticable.email}] {self.name}'