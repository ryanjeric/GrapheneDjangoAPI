import graphene
import graphql_jwt
import project.sampleapp.schema
import project.users.schema

class Query(
    project.users.schema.Query,
    project.sampleapp.schema.Query,
    graphene.ObjectType):

    pass

class Mutation(
    project.users.schema.Mutation,
    project.sampleapp.schema.Mutation,
    graphene.ObjectType):

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)