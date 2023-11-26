"""Parse pydantic 1.10 module to mermaid graph"""
from types import ModuleType
from typing import Any, Dict, List, Set, Type

# MAPPING_LIKE_SHAPES is in pydantic 1.10 not in 1.7
from pydantic.fields import MAPPING_LIKE_SHAPES, ModelField, SHAPE_SINGLETON
from pydantic.main import ModelMetaclass
from pydantic.typing import get_args, get_origin, is_union, WithArgsTypes

from pydantic_mermaid.models import MermaidClass, MermaidGraph, Property


base_types = [str, int, float, bool]

# constrained types are generated dynamically we can only remove them by name
constrained_types = {
    "ConstrainedStrValue",
    "ConstrainedFloatValue",
    "ConstrainedIntValue",
    "ConstrainedSetValue",
    "ConstrainedFrozenSetValue",
    "ConstrainedListValue",
    "ConstrainedDecimalValue",
    "ConstrainedDateValue",
}


def _get_dependencies(v: Type[Any]) -> Set[str]:
    """get dependencies from property types"""
    ans: Set[str] = set()
    if v in base_types:
        return ans

    if not isinstance(v, WithArgsTypes) and not isinstance(v, type):
        return ans

    if is_union(get_origin(v)):
        for sub_v in get_args(v):
            ans |= _get_dependencies(sub_v)
        return ans

    if "__args__" in dir(v):
        for sub_v in get_args(v):
            ans |= _get_dependencies(sub_v)
        return ans
        # Generic alias are constructs like `list[int]`

    return {v.__name__} - constrained_types


def _get_field_dependencies(field: ModelField) -> Set[str]:
    ans = set()
    if field.shape == SHAPE_SINGLETON:
        ans |= _get_dependencies(field.type_)
    elif field.shape in MAPPING_LIKE_SHAPES:
        ans |= _get_dependencies(field.key_field.type_)  # type: ignore
        ans |= _get_dependencies(field.type_)

    if field.sub_fields is not None:
        for sub_field in field.sub_fields:  # type: ignore
            ans |= _get_field_dependencies(sub_field)

    return ans


class PydanticParser:
    """parse pydantic module to mermaid graph"""

    def __call__(self, module: ModuleType) -> MermaidGraph:
        graph = MermaidGraph()

        """extrac information from module"""
        for class_name, class_type in module.__dict__.items():
            if class_name in ["BaseModel"]:
                continue

            properties: List[Property] = []

            if not isinstance(class_type, ModelMetaclass):
                continue

            # inheritance
            parents = class_type.mro()
            first_parent = parents[1]
            parent_name = first_parent.__name__
            graph.child_parents[class_name] = {parent_name}
            if parent_name in graph.classes:
                if parent_name not in graph.parent_children:
                    graph.parent_children[parent_name] = set()
                graph.parent_children[parent_name].add(class_name)

            # fields
            fields: Dict[str, ModelField] = class_type.__fields__
            graph.service_clients[class_name] = set()
            for field_name, field in fields.items():
                properties.append(Property(name=field_name, type=field._type_display()))
                # dependencies
                graph.service_clients[class_name] = graph.service_clients[class_name] | _get_field_dependencies(field)

            graph.service_clients[class_name] = graph.service_clients[class_name]
            graph.classes[class_name] = MermaidClass(name=class_name, properties=properties)

        return graph
