from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
        def create_user(self, email, username, name, last_name, password = None):
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
            return superuser

class User(AbstractBaseUser):
    username = models.CharField('User name', unique=True, max_length=100)
    email = models.EmailField('Email', max_length=254, unique=True)
    name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    image = models.ImageField('Profile image', upload_to='profile/', blank= True, null= True, max_length=200)
    active_user = models.BooleanField(default = True)
    admin_user = models.BooleanField(default = False)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']
    
    def __str__(self, *args, **kwargs):
        return f"{self.name},{self.last_name}"
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.admin_user