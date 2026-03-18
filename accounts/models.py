from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('AGENCY_ADMIN', 'Agency Admin'),
        ('SUBCITY_ADMIN', 'Sub City Admin'),
        ('WOREDA_ADMIN', 'Woreda Admin'),
        ('WOREDA_STAFF', 'Woreda Staff'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    agency = models.ForeignKey('locations.Agency', on_delete=models.SET_NULL, null=True, blank=True)
    sub_city = models.ForeignKey('locations.SubCity', on_delete=models.SET_NULL, null=True, blank=True)
    woreda = models.ForeignKey('locations.Woreda', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
