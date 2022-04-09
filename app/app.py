from typing import Optional

import strawberry
from attrs import define
from backports.cached_property import cached_property
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import ScopedSession
from starlette.applications import Starlette
from strawberry import Schema
from strawberry.asgi import GraphQL
from yaml import safe_load


@define(slots=False)
class LabyrinthApplication:
    configuration_path: str
    _sessionmaker: Optional[sessionmaker] = None

    @cached_property
    def conf(self) -> dict:
        with open(self.configuration_path) as file:
            _conf = safe_load(file)
        return _conf

    @property
    def session(self) -> ScopedSession:
        if not self._sessionmaker:
            engine = create_engine(self.conf["sqlalchemy_url"])
            self._sessionmaker = sessionmaker(engine, future=True)
        return ScopedSession(self._sessionmaker)

    # TODO: move in CLI? Or somewhere else, it shouldn't be in the app.
    def create_database(self):
        from app.configuration.database import Base

        # TODO: make sure to import all models so that Base.metadata is properly populated.
        Base.metadata.create_all(self.sessionmaker.kw["bind"])

    def create_starlette_app(self) -> Starlette:
        from schema.mutations.construction.players.items import Mutation as PlayerMutation
        from schema.queries.construction.players import Query as PlayerQuery

        @strawberry.type
        class Query(PlayerQuery):
            ...

        @strawberry.type
        class Mutation(PlayerMutation):
            ...

        schema = Schema(query=Query, mutation=Mutation)
        graphql_schema = GraphQL(schema)

        app = Starlette()
        app.add_route("/graphql", graphql_schema)
        return app
