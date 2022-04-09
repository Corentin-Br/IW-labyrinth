from typing import Generator, Tuple

import pytest
from sqlalchemy.orm import Session, sessionmaker
from starlette.testclient import TestClient

from app.api import get_app, setup_app
from app.app import LabyrinthApplication
from models.players.item import ItemSaModel
from schema.dataclasses.players import Item
from utils.dataclass_mapper import turn_in_dataclass
from utils.sqlalchemy import create_metadata, get_engine


@pytest.fixture(autouse=True, scope="session")
def test_app() -> LabyrinthApplication:
    setup_app(configuration_path="test_conf.yaml")
    create_metadata(get_engine(get_app().session))
    return get_app()


@pytest.fixture(autouse=True, scope="session")
def test_client(test_app: LabyrinthApplication) -> Generator[TestClient, None, None]:
    with TestClient(test_app.create_starlette_app()) as _client:
        yield _client


@pytest.fixture(autouse=True)
def test_session(test_app: LabyrinthApplication) -> Generator[Session, None, None]:

    engine = get_engine(test_app.session)
    _conn = engine.connect()
    _trans = _conn.begin()
    test_app._sessionmaker = sessionmaker(bind=_conn, future=True)

    yield test_app.session()

    test_app.session.close()
    _trans.rollback()
    _conn.close()


@pytest.fixture
def item_tuple(test_app: LabyrinthApplication, test_client: TestClient) -> Tuple[Item, ItemSaModel]:
    with test_app.session() as session, session.begin():
        item = ItemSaModel(name="item", rank=1)
        session.add(item)
        session.flush()
        return turn_in_dataclass(item, Item), item
