from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings

# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user(
        self,
        name,
        email,
        password,
    ):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Model for user profile"""

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password"]

    class Meta:
        db_table = "user_profile"

    def get_full_name(self):
        """get full name of user"""
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """Profile feed update"""

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return model as str"""
        return self.status_text
