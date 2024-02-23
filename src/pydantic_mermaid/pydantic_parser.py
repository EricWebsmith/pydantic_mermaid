"""Parse pydantic 1.10 module to mermaid graph"""
from enum import EnumMeta
from types import ModuleType
from typing import Any, Dict, List, Set, Type

from pydantic.fields import SHAPE_SINGLETON, ModelField
from pydantic.main import ModelMetaclass

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

    return {v.__name__} - constrained_types


def _get_field_dependencies(field: ModelField) -> Set[str]:
    ans = set()

    if field.key_field is not None:
        ans |= _get_field_dependencies(field.key_field)

    if field.shape == SHAPE_SINGLETON and not field.sub_fields:
        ans |= _get_dependencies(field.type_)

    # We can use sub_fields to get the type of the elements in a List, Union, etc.
    if field.sub_fields is not None:
        for sub_field in field.sub_fields:
            ans |= _get_field_dependencies(sub_field)

    return ans


def get_default_value(field: ModelField) -> str:
    default_value = ""
    if not field.required:
        if isinstance(field.default, str) and not isinstance(field.type_, EnumMeta):
            default_value = f"'{field.default}'"
        else:
            default_value = str(field.default)

    return default_value


class PydanticParser:
    """parse pydantic module to mermaid graph"""

    def __call__(self, module: ModuleType) -> MermaidGraph:
        graph = MermaidGraph()

        """extract information from module"""
        for class_name, class_type in module.__dict__.items():
            if class_name in ["BaseModel", "Enum", "Extra", "Relations"]:
                continue

            if type(class_type) not in [ModelMetaclass, EnumMeta]:
                continue

            # inheritance
            parents = class_type.mro()
            first_parent = parents[1]
            parent_name = first_parent.__name__
            graph.child_parents[class_name] = {parent_name}
            if parent_name in graph.class_dict:
                if parent_name not in graph.parent_children:
                    graph.parent_children[parent_name] = set()
                graph.parent_children[parent_name].add(class_name)

            # fields
            annotation = ""
            properties: List[Property] = []
            if isinstance(class_type, ModelMetaclass):
                fields: Dict[str, ModelField] = class_type.__fields__
                graph.service_clients[class_name] = set()
                for field_name, field in fields.items():
                    # earlier than pydantic 1.9, _type_display will print out a long ugly string

                    properties.append(
                        Property(name=field_name, type=field._type_display(), default_value=get_default_value(field))
                    )
                    # dependencies
                    graph.service_clients[class_name] = graph.service_clients[class_name] | _get_field_dependencies(
                        field
                    )
                graph.service_clients[class_name] = graph.service_clients[class_name]
            elif isinstance(class_type, EnumMeta):
                annotation = "Enumeration"
                for name, member in class_type._member_map_.items():
                    field_type = type(member.value).__name__
                    value = f"'{member.value}'" if isinstance(member.value, str) else str(member.value)
                    properties.append(Property(name=name, type=field_type, default_value=value))

            graph.class_dict[class_name] = MermaidClass(name=class_name, properties=properties, annotation=annotation)
            graph.class_names.append(class_name)

        return graph
