from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from api.models import Franchise, Property, Service, Job, Activity


class FranchiseType(DjangoObjectType):
    class Meta:
        model = Franchise
        fields = "__all__"


class PropertyType(DjangoObjectType):
    class Meta:
        model = Property
        fields = "__all__"


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        fields = "__all__"


class JobType(DjangoObjectType):
    class Meta:
        model = Job
        fields = "__all__"


class ActivityType(DjangoObjectType):
    class Meta:
        model = Activity
        fields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
