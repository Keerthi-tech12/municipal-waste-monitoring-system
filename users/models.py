from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = [

        ('Commissioner', 'Commissioner'),
        ('Zone Officer', 'Zone Officer'),
        ('Data Entry Operator', 'Data Entry Operator'),

    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES
    )

    def __str__(self):

        return f"{self.user.username} - {self.role}"