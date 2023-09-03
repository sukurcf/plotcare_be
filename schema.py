import graphene
from django.contrib.auth.models import User

from _graphql.types import UserType
from _graphql.crud.activity import ActivityCreation, ActivityUpdation, ActivityDeletion


class Query(graphene.ObjectType):
    # all_properties = DjangoListField(PropertyType)
    # all_services = DjangoListField(ServiceType)
    # all_franchises = DjangoListField(FranchiseType)
    # all_jobs = DjangoListField(JobType)
    # all_activities = DjangoListField(ActivityType)
    # all_users = DjangoListField(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_activity = ActivityCreation.Field()
    update_activity = ActivityUpdation.Field()
    delete_activity = ActivityDeletion.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
