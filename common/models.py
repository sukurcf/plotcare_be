from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.constants import STATE_CHOICES


# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=50)
    line1 = models.CharField(max_length=30)
    line2 = models.CharField(max_length=30)
    town = models.CharField(max_length=40)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    pincode = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])

    class Meta:
        abstract = True


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
