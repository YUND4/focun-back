from django.contrib.auth.models import BaseUserManager
from django.db import IntegrityError, models, transaction
from common.utils import get_model

class AuthenticableManager(BaseUserManager):

    @property
    def admin_model(self):
        return get_model('users.Admin')

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is required')
        authenticable = self.model(email=self.normalize_email(email))
        authenticable.set_password(password)
        authenticable.save(using=self._db)
        return authenticable

    def create_superuser(self, email, password, ip='0.0.0.0'):
        authenticable = self.create_user(email, password=password)
        authenticable.is_superuser = True
        authenticable.admin = self.admin_model(ip=ip)
        authenticable.save(using=self._db)
        return authenticable
    
class UserManager(models.Manager):

    @property
    def profile_model(self):
        return get_model('users.Profile')
    
    @property
    def authenticable_model(self):
        return get_model('users.Authenticable')

    def create_complete_user(self,
        email: str,
        password: str,
        name: str,
        last_name: str,
        description: str,
        country: str,
        phone: str,
    ):
        with transaction.atomic():

            authenticable = self.authenticable_model.objects.create_user(
                email=email,
                password=password
            )
            
            user = self.model(
                name=name,
                last_name=last_name,
                authenticable=authenticable
            )

            user.save(using=self._db)

            self.profile_model.objects.create(
                description=description,
                country=country,
                phone=phone,
                user=user
            )
            
            return user