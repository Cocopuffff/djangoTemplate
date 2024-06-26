from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Custom user model to override BaseUserManager defaults to create the account in the database.
class AccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have a valid email')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=email,
            name=name,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    name = models.CharField(max_length=30)
    # auto_now_add adds it once when created
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    # auto_now updates whenever it is accessed
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # access Account Manager
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    # has permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # to further customise access to module by adding @ declarator in module
    def has_module_perms(self, app_label):
        return True