from types import ModuleType
from typing import Type, Any

from pydantic import BaseModel
from pydantic.fields import ModelField, MAPPING_LIKE_SHAPES, SHAPE_SINGLETON
from pydantic.main import ModelMetaclass
from pydantic.typing import get_origin, is_union, WithArgsTypes, get_args


try:
    from typing import GenericAlias as TypingGenericAlias  # type: ignore
except ImportError:
    # python < 3.9 does not have GenericAlias (list[int], tuple[str, ...] and so on)
    TypingGenericAlias = ()


class Property(BaseModel):
    name: str
    type: str


class ClassType(BaseModel):
    name: str
    properties: list[Property]

    def __str__(self) -> str:
        s = f"\n    class {self.name} {{\n"
        for property in self.properties:
            s += f"        {property.name}: {property.type}\n"
        s += "    }\n"
        return s


base_types = [str, int, float, bool, dict]
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


def get_dependencies(v: Type[Any]) -> set[str]:
    ans: set[str] = set()
    if v in base_types:
        return ans

    if not isinstance(v, WithArgsTypes) and not isinstance(v, type):
        return ans

    if is_union(get_origin(v)):
        for sub_v in get_args(v):
            ans |= get_dependencies(sub_v)
        return ans

    if "__args__" in dir(v):
        for sub_v in get_args(v):
            ans |= get_dependencies(sub_v)
        return ans
        # Generic alias are constructs like `list[int]`

    return {v.__name__} - constrained_types


def _get_field_dependencies(field: ModelField) -> set[str]:
    ans = set[str]()
    if field.shape == SHAPE_SINGLETON:
        ans |= get_dependencies(field.type_)
    elif field.shape in MAPPING_LIKE_SHAPES:
        ans |= get_dependencies(field.key_field.type_)  # type: ignore
        ans |= get_dependencies(field.type_)

    if field.sub_fields is not None:
        for sub_field in field.sub_fields:  # type: ignore
            ans |= _get_field_dependencies(sub_field)

    return ans


class MermaidGenerator:
    def __init__(self, module: ModuleType) -> None:
        self.classes: list[ClassType] = []
        self.dependencies: dict[str, set[str]] = {}
        self.inheritances: dict[str, set[str]] = {}

        class_set = set[str]()
        for class_name, class_type in module.__dict__.items():
            if class_name in ['BaseModel']:
                continue

            properties: list[Property] = []
            if isinstance(class_type, ModelMetaclass):
                # inheritance
                parents = class_type.mro()
                first_parent = parents[1]
                parent_name = first_parent.__name__
                if parent_name in class_set:
                    if parent_name not in self.inheritances:
                        self.inheritances[parent_name] = set[str]()
                    self.inheritances[parent_name].add(class_name)

                # fields
                fields: dict[str, ModelField] = class_type.__fields__
                self.dependencies[class_name] = set[str]()
                for field_name, field in fields.items():
                    properties.append(Property(name=field_name, type=field._type_display()))
                    # dependencies
                    self.dependencies[class_name] = self.dependencies[class_name] | _get_field_dependencies(field)
                self.dependencies[class_name] = self.dependencies[class_name] & class_set
                class_set.add(class_name)
                self.classes.append(ClassType(name=class_name, properties=properties))

    def generate_chart(self, root: str = "") -> str:

        allow_list = set[str]([root])
        if root != "":
            for dependant in self.dependencies.__reversed__():
                if dependant in allow_list:
                    allow_list = allow_list | self.dependencies[dependant]
        else:
            allow_list = {c.name for c in self.classes}

        s = "```mermaid\nclassDiagram"
        for c in self.classes:
            if c.name not in allow_list:
                continue
            s += str(c)

        s += "\n\n"

        for dependant, depended in self.dependencies.items():
            if dependant not in allow_list:
                continue

            for d in depended:
                if d not in allow_list:
                    continue
                s += f"    {dependant} ..> {d}\n"

        s += "\n"

        for parent, children in self.inheritances.items():
            for child in children:
                s += f"    {parent} <|-- {child}\n"

        s += "```"
        return s
