from typing import Any, Type, TypeVar

from attr import fields, has
from cattrs import Converter
from cattrs.gen import make_dict_unstructure_fn, override

from app.configuration.database import Base

D = TypeVar("D", bound=Base)
T = TypeVar("T")
_converter = None


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.capitalize() for x in components[1:])


class SqlAlchemyConverter(Converter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.register_unstructure_hook_factory(has, self.to_camel_case_unstructure)
        self._structure_func.register_func_list([(has, self.structure_attrs_from_sa_model)])

    def structure_attrs_from_sa_model(self, obj: D, cl: Type[T]) -> T:
        """Instantiate an attrs class from a sql alchemy model"""

        conv_obj = {}
        for a in fields(cl):  # type: ignore
            name = a.name
            val = getattr(obj, name)
            conv_obj[name] = self._structure_attribute(a, val)

        return cl(**conv_obj)  # type: ignore

    def to_camel_case_unstructure(self, cls: Any) -> Any:
        return make_dict_unstructure_fn(
            cls, self, **{a.name: override(rename=to_camel_case(a.name)) for a in fields(cls)}
        )


def get_converter() -> SqlAlchemyConverter:
    global _converter
    if not _converter:
        _converter = SqlAlchemyConverter()
    return _converter


def turn_in_dataclass(obj: D, cl: Type[T]) -> T:
    return get_converter().structure_attrs_from_sa_model(obj, cl)


def to_camel_case_unstructure(obj: Any) -> Any:
    return get_converter().unstructure(obj)
