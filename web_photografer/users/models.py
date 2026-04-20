from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MODERATOR = 'MODERATOR', 'Moderator'
        USER = 'USER', 'User'
    
    bio = models.TextField('Биография', blank=True)

    avatar = models.ImageField('Аватар', upload_to='avatars/',blank=True, null=True)

    role = models.CharField(
        'роль',
        max_length=15,
        choices = Roles.choices,
        default = Roles.USER
    )

    def __str__(self):
        return self.username