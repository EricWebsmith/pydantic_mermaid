"""Parse pydantic 1.10 module to mermaid graph"""
from types import ModuleType
from typing import Any, Dict, List, Set, Type

from pydantic.fields import ModelField, SHAPE_SINGLETON
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
    print('v', v)
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
        print("field.sub_fields", field.sub_fields)
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
                # earlier than pydantic 1.9, _type_display will print out a long ugly string
                properties.append(Property(name=field_name, type=field._type_display()))
                # dependencies
                graph.service_clients[class_name] = graph.service_clients[class_name] | _get_field_dependencies(field)

            graph.service_clients[class_name] = graph.service_clients[class_name]
            graph.classes[class_name] = MermaidClass(name=class_name, properties=properties)

        return graph
