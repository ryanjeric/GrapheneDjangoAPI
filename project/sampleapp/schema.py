import graphene

from graphene_django import DjangoObjectType
from project.sampleapp.models import Sampletbl



## JWT DECORATORS ( AUTHENTACATION/AUTHORIZATION )
## https://django-graphql-jwt.domake.io/en/stable/decorators.html
from graphql_jwt.decorators import login_required # @login_required
from graphql_jwt.decorators import permission_required # @permission_required('auth.delete_user')

#from var_dump import var_dump

from project.users.schema import UserType


class SampletblType(DjangoObjectType):
    class Meta:
        model = Sampletbl
        #exclude_fields = ('createdby') # Limiting field access on GRAPHQL
# CREATE
class CreateSampletbl(graphene.Mutation):
    id = graphene.Int()
    col1 = graphene.String()
    col2 = graphene.String()
    createdby = graphene.Field(UserType)

    class Arguments:
        col1 = graphene.String()
        col2 = graphene.String()

    @login_required
    def mutate(self, info, col1, col2):

        # ADDING AUTHORIZATION ON MUTATION
        # user = info.context.user
        # if not user.is_authenticated:
        #     raise Exception('Authentication credentials were not provided')
        # if user.is_anonymous:
        #     raise Exception('Not logged in!')

        user = info.context.user #or None -> add if not required
        tbl = Sampletbl(col1=col1,col2=col2,createdby=user)
        tbl.save()
        return CreateSampletbl(
            id=tbl.id,
            col1=tbl.col1,
            col2=tbl.col2,
            createdby=tbl.createdby
        )

# UPDATE
class UpdateSampletbl(graphene.Mutation):
    id = graphene.Int()
    col1 = graphene.String()
    col2 = graphene.String()
    

    class Arguments:
        id = graphene.Int()
        col1 = graphene.String()
        col2 = graphene.String()


    def mutate(self, info, id, col1, col2):
        tbl = Sampletbl.objects.get(pk=id)
        tbl.col1 = col1
        tbl.col2 = col2
        tbl.save()

        return UpdateSampletbl(
            id=tbl.id,
            col1=tbl.col1,
            col2=tbl.col2
        )    

# DELETE
class DeleteSampletbl(graphene.Mutation):
    id = graphene.Int()
    class Arguments:
        id = graphene.Int()
    
    @permission_required('sampleapp.delete_sampletbl')
    def mutate(self, info, id):
        tbl = Sampletbl.objects.get(pk=id)
        tbl.delete()

        return DeleteSampletbl(
            id=id
        )


class Query(object): ## RETRIEVE
    #getting singlerecord
    sampletbl = graphene.Field(SampletblType,id=graphene.Int(),col1=graphene.String())

    #listall
    all_sampletbl = graphene.List(SampletblType)

    paginate_sampletbl = graphene.List(SampletblType,first=graphene.Int(),skip=graphene.Int())

    def resolve_all_sampletbl(self,info,**kwargs):
        # ADDING AUTHORIZATION ON QUERY
        #user = info.context.user
        #if user.is_anonymous:
        #     raise Exception('Not logged in!')
        return Sampletbl.objects.all()


    def resolve_paginate_sampletbl(self,info,first=None,skip=None,**kwargs):
        dta = Sampletbl.objects.all()

        if skip:
            dta = dta[skip:]
        if first:
            dta = dta[:first]
        return dta

    def resolve_sampletbl(self, info, **kwargs):
        id = kwargs.get('id')
        col1 = kwargs.get('col1')

        if id is not None:
            return Sampletbl.objects.get(pk=id)
        if col1 is not None:
            return Sampletbl.objects.get(col1=col1)
        
        return None

class Mutation(graphene.ObjectType):
    create_sampletbl = CreateSampletbl.Field()
    update_sampletbl = UpdateSampletbl.Field()
    delete_sampletbl = DeleteSampletbl.Field()