from django.contrib.auth.models import BaseUserManager

class AuthenticableManager(BaseUserManager):

    @property
    def admin_model(self):
        module = __import__('users.models', fromlist=['Admin'])
        return getattr(module, 'Admin')

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, ip='0.0.0.0'):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.admin = self.admin_model(ip=ip)
        user.save(using=self._db)
        return user