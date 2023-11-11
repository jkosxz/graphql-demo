import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

class Query (graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value=", World 🌎 !"))
    def resolve_hello(self, info, name):
        return "Hello " + name

app = FastAPI()

app.mount("/",GraphQLApp(schema=graphene.Schema(query=Query),on_get=make_graphiql_handler()))
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))