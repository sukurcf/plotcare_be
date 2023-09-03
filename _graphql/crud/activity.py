import graphene

from api.models import Activity
from _graphql.types import ActivityType


class ActivityCreation(graphene.Mutation):
    class Arguments:
        job = graphene.Int(required=True)
        created_by = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    activity = graphene.Field(ActivityType)

    @classmethod
    def mutate(cls, root, info, job, created_by, name, description):
        activity = Activity(
            job_id=job,
            created_by_id=created_by,
            name=name,
            description=description
        )
        activity.save()
        return ActivityCreation(activity=activity)


class ActivityUpdation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        job = graphene.Int(required=True)
        created_by = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    activity = graphene.Field(ActivityType)

    @classmethod
    def mutate(cls, root, info, id, job, created_by, name, description):
        activity = Activity.objects.get(pk=id)
        activity.job_id = job
        activity.created_by_id = created_by
        activity.name = name
        activity.description = description
        activity.save()
        return ActivityUpdation(activity=activity)


class ActivityDeletion(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    activity = graphene.Field(ActivityType)

    @classmethod
    def mutate(cls, root, info, id):
        activity = Activity.objects.get(pk=id)
        activity.delete()
        return ActivityDeletion(activity=activity)
