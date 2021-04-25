from django.db import models
from django.utils.timezone import now
from django.utils.translation import pgettext_lazy
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.


class UserManager(BaseUserManager):

    def get_user(self, email):
        email = UserManager.normalize_email(email)
        return self.model(email=email, is_active=True)
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class User(AbstractBaseUser):
    """
    add fields if you want.
    """
    email = models.EmailField(unique=True)

    # extra fields..
    fname = models.CharField(max_length=25, null=True)
    lname = models.CharField(max_length=25, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=now, editable=False)
    # username = None 
    USERNAME_FIELD = 'email'   
    objects = UserManager()

    class Meta:

        ordering = ('-id',)
        permissions = (

            # ('view_user',
            #  pgettext_lazy('Permission description', 'Can view users')),
            ('edit_user',
             pgettext_lazy('Permission description', 'Can edit users')),

            ('view_group',
             pgettext_lazy('Permission description', 'Can view groups')),
            ('edit_group',
             pgettext_lazy('Permission description', 'Can edit groups')),

            ('view_staff',
             pgettext_lazy('Permission description', 'Can view staff')),
            ('edit_staff',
             pgettext_lazy('Permission description', 'Can edit staff')),

            ('impersonate_user',
             pgettext_lazy('Permission description', 'Can impersonate users'))
        )
