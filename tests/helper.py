import uuid
from enum import Enum
from typing import Any, Optional, Tuple, Type, Union, cast

from strawberry import LazyType
from strawberry.type import StrawberryList, StrawberryOptional, StrawberryType

from utils.dataclass_mapper import to_camel_case


def get_fields_as_string(class_: Union[Optional[Type], StrawberryType], with_children: bool = True) -> str:
    result = ""
    if isinstance(class_, LazyType):
        class_ = class_.resolve_type()

    if hasattr(class_, "_type_definition"):
        class_ = cast(Type, class_)  # mypy doesn't understand the hasattr.
        result += "{\n"
        for field in class_._type_definition.fields:
            if hasattr(field.type, "_type_definition"):
                if with_children:
                    result += (
                        f"{to_camel_case(field.name)}"
                        f"{get_fields_as_string(field.type, with_children=with_children)}"
                    )
                else:
                    raise Exception(
                        f"The attributes {field.name} of type {field.type.__name__} in dataclass {class_.__name__} "
                        f"must be Optional."
                    )
            elif isinstance(field.type, (StrawberryList, StrawberryOptional)):
                child_type = field.type.of_type
                while hasattr(child_type, "of_type"):
                    child_type = child_type.of_type  # type: ignore
                    # if we have Optional[List] for example.
                if hasattr(child_type, "_type_definition") or isinstance(child_type, LazyType) and not with_children:
                    continue
                result += (
                    f"{to_camel_case(field.name) }" f"{get_fields_as_string(field.type, with_children=with_children)}"
                )
            else:
                result += f"{to_camel_case(field.name)}\n"
        result += "}\n"
    else:
        result = "\n"
    return result


def get_graphql_query_string(
    class_: Optional[Type], query_type: str, query_name: str, with_children: bool = True
) -> str:
    return f"{query_type} {{\n{query_name}(%s) {get_fields_as_string(class_, with_children=with_children)}}}"


def generic_queries(class_: Type, query_name: Optional[str] = None) -> Tuple[str, str, str, str, str]:
    if query_name is None:
        last_char = class_.__name__[-1]
        query_name = (
            f"{class_.__name__[0].lower()}{class_.__name__[1:-1]}" f"{'ies' if last_char == 'y' else f'{last_char}s'}"
        )
    return (
        get_graphql_query_string(class_, "query", query_name),
        get_graphql_query_string(class_, "query", query_name, with_children=False),
        get_graphql_query_string(class_, "mutation", f"create{class_.__name__}"),
        get_graphql_query_string(class_, "mutation", f"update{class_.__name__}"),
        get_graphql_query_string(None, "mutation", f"delete{class_.__name__}"),
    )


def to_graphql_inputs(**kwargs: Any) -> str:
    def get_str_value(value: Any) -> str:
        if isinstance(value, list):
            if not value:
                return "[]"
            else:
                return "[" + ",".join(get_str_value(sub_value) for sub_value in value) + "]"
        if isinstance(value, (str, uuid.UUID)):
            return '"' + str(value) + '"'
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, dict):
            return "{" + to_graphql_inputs(**value) + "}"
        if value is None:
            return "null"
        if isinstance(value, Enum):
            return cast(str, value)
        else:
            return str(value)

    return ", ".join(f"{key}: {get_str_value(value)}" for key, value in kwargs.items())


def get_graphql_query(query: str, **kwargs: Any) -> dict:
    return {"query": query % to_graphql_inputs(**kwargs) if kwargs else {"query": query.replace("(%s)", "")}}
