from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Model for user profile"""
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True,null=False)
    password = models.CharField(max_length=255, null=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['name','password']
    
    class Meta:
        db_table = "user_profile"
    
    def get_full_name(self):
        """get full name of user"""
        return self.name
    
    def __str__(self):
        return self.email
    
    def create_user(
        name,
        email,
        password=None,
        is_active=1,
        is_staff=0
    ):
        user = UserProfile.objects.get(email=email)
        if user:
            return user
        else:
            user = UserProfile()
            user.name = name
            user.email = email
            user.password = password
            user.is_active = is_active
            user.is_staff=is_staff
        
            user.save()
            return user
        
    def create_super_user(
        name,
        email,
        password
    ):
        user = UserProfile.create_user(name,email,password)
        user.is_superuser=True
        
        user.save()
        return user
    