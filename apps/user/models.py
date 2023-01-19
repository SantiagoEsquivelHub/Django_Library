from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, username, name, last_name, is_staff, is_superuser, password, **extra_fields):
        user = self.model(
                username = username,
                email = self.normalize_email(email),
                name = name,
                last_name = last_name,
                is_staff = is_staff,
                is_superuser = is_superuser,
                **extra_fields
            )
        
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_user(self, email, username, name, last_name, **extra_fields):
        return self._create_user(email, username, name, last_name, is_staff = False, is_superuser = False, **extra_fields)
    
    
    def create_superuser(self, email, username, name, last_name, **extra_fields):
        return self._create_user(email, username, name, last_name, is_staff = True, is_superuser = True, **extra_fields)   
            
        """ def create_user(self, email, username, name, last_name, password = None):
            if not email:
                raise ValueError('The user has to have a email')
            
            user = self.model(
                username = username,
                email = self.normalize_email(email),
                name = name,
                last_name = last_name,
            )
            
            user.set_password(password)
            user.save()
            return user
        
        def create_superuser(self, email, username, name, last_name, password):

            superuser = self.create_user(
                username = username,
                email = email,
                name = name,
                last_name = last_name,
                password = password
            )
            
            superuser.admin_user = True
            superuser.save()
            return superuser """

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=254, unique=True)
    username = models.CharField('User name', unique=True, max_length=100)
    name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    image = models.ImageField('Profile image', upload_to='profile/', blank= True, null= True, max_length=200)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']
    
    def __str__(self, *args, **kwargs):
        return f"{self.name}, {self.last_name}"
    
