from django.contrib.auth.models import User
from django.db import models

from common.constants import PROPERTY_TYPES, PROPERTY_STATUSES, SERVICE_TYPES, SERVICE_STATUSES
from common.models import Address, TimestampModel


class Franchise(Address, TimestampModel):
    name = models.CharField(max_length=20)
    description = models.TextField(default=None)


class Property(Address, TimestampModel):
    class Meta:
        verbose_name_plural = "Properties"

    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
    type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=10, choices=PROPERTY_STATUSES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Service(TimestampModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=False)
    description = models.TextField(default=None)
    type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    status = models.CharField(max_length=20, choices=SERVICE_STATUSES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Job(TimestampModel):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_to")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")


class Activity(TimestampModel):
    job = models.ForeignKey(Job, models.CASCADE)
    created_by = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
