from typing import Tuple

from sqlalchemy import select
from starlette.testclient import TestClient

from app.app import LabyrinthApplication
from models.players.item import ItemSaModel
from schema.dataclasses.players import Item
from tests.helper import generic_queries, get_graphql_query
from utils.dataclass_mapper import to_camel_case_unstructure, turn_in_dataclass

get_item_query, _, create_item_mutation, update_item_mutation, delete_item_mutation = generic_queries(Item)


def test_create_item(test_app: LabyrinthApplication, test_client: TestClient) -> None:
    expected_item = {"name": "an item", "rank": 1}
    # TODO: add DBStatementTestInspector
    with test_app.session() as session:
        response = test_client.post("/graphql", json=get_graphql_query(create_item_mutation, inputs=expected_item))
        assert response.status_code == 200
        new_item_orm = session.execute(select(ItemSaModel).where(ItemSaModel.name == "an item")).scalar_one()
        assert response.json() == {
            "data": {"createItem": to_camel_case_unstructure(turn_in_dataclass(new_item_orm, Item))}
        }


def test_update_item(
    test_app: LabyrinthApplication, test_client: TestClient, item_tuple: Tuple[Item, ItemSaModel]
) -> None:
    item_dc, _ = item_tuple
    expected_item: dict = {"name": "an updated item", "rank": 5}
    # TODO: add DBStatementTestInspector
    with test_app.session() as session:  # noqa
        response = test_client.post(
            "/graphql", json=get_graphql_query(update_item_mutation, inputs={**expected_item, "itemId": item_dc.id})
        )
        assert response.status_code == 200
        assert response.json() == {"data": {"updateItem": {**expected_item, "id": item_dc.id}}}


def test_get_item(
    test_app: LabyrinthApplication, test_client: TestClient, item_tuple: Tuple[Item, ItemSaModel]
) -> None:
    item_dc, _ = item_tuple
    with test_app.session() as session:  # noqa
        response = test_client.post("/graphql", json=get_graphql_query(get_item_query, itemIds=[item_dc.id]))
        assert response.status_code == 200
        assert response.json() == {"data": {"items": [to_camel_case_unstructure(item_dc)]}}
