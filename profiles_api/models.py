from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """
    def create_user(self, email, name, password=None):
        """
        Create a new user profile
        """
        if not email:
            raise ValueError("Please Provide an Email Address!")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        ## Saving to the provided databse.
        ## will need to change if using Mongo.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser with given details.
        """
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    This is the database model for users in the system.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) ## is user activated?
    is_staff = models.BooleanField(default=False) ## default users are not staff.

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        retrieve full name of user.
        """
        return self.name

    def get_short_name(self):
        """
        retrieve short name of user.
        """
        return self.name

    def __str__(self):
        """
        Return string representation of our user

        Note: recommended for all django models to identify
        the object (in this case, a user).
        """
        return self.email
