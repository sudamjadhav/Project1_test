from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    - Creating custom user model where email is used for authentication insted of username.
    """

    def create_user(self, email, password, **extra_fields):
        """
        - Create and save user with email and password both are mandatory fields.
        """

        if not email:
            """To ensure user created with valid email address"""
            raise ValueError(_("Email must set."))
        
        email = self.normalize_email(email)     # normalize_email: convert text into lowercase
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is False:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_active') is False:
            raise ValueError(_('Superuser must have is_active=True'))
        if extra_fields.get('is_superuser') is False:
            raise ValueError(_('Superuser must have is_superuser=True'))
        
        return self.create_user(email, password, **extra_fields)

