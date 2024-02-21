from enum import Flag, auto
from typing import Dict, List, Set

from pydantic import BaseModel, Field


class Relations(Flag):
    """Enum for representing the different types of relationships between classes."""

    Inheritance = auto()
    Dependency = auto()
    Both = Inheritance | Dependency

    def __str__(self) -> str:
        if isinstance(self.name, str):
            return self.name.lower()

        return ""  # pragma: no cover

    def __repr__(self) -> str:  # pragma: no cover
        return str(self)

    @staticmethod
    def parse(s: str) -> "Relations":
        """Convert a string to a Relations enum"""

        return Relations[s.title()]


class Property(BaseModel):
    """A class representing a property of a MermaidClass."""

    name: str
    type: str
    default_value: str = ""

    def __str__(self) -> str:
        s = f"{self.name}: {self.type}"
        if self.default_value:
            s = s + f" = {self.default_value}"

        return s


class MermaidClass(BaseModel):
    """We call it mermaid class because 'class' is a keyword"""

    name: str
    properties: List[Property]
    annotation: str = ""

    def __str__(self) -> str:
        return self.generate_class(set())

    def generate_class(self, exclude: Set[str]) -> str:
        """
        Generate mermaid class definition with some properties omitted.
        This is used when there is a parent class and we want to omit inherited properties.

        :param exclude: A set of '{property.name}: {property.type}' to be excluded from the generated class definition.
        """
        # flake8 of python3.12 treats class as a keyword and gives the following error:
        # ./src/pydantic_mermaid/models.py:40:17: E272 multiple spaces before keyword
        s = f"\n{'    '}class {self.name} {{\n"
        if self.annotation:
            s += f"        <<{self.annotation}>>\n"
        for property in self.properties:
            property_with_type = str(property)
            if property_with_type in exclude:
                continue
            s += f"        {property_with_type}\n"
        s += "    }\n"
        return s


class MermaidGraph(BaseModel):
    """A graph of mermaid classes and their relationships"""

    class_names: List[str] = Field(
        description="A list of all pydantic classes that is topologically sorted",
        default_factory=list,
    )
    class_dict: Dict[str, MermaidClass] = Field(default_factory=dict)
    service_clients: Dict[str, Set[str]] = Field(default_factory=dict)
    client_services: Dict[str, Set[str]] = Field(default_factory=dict)
    parent_children: Dict[str, Set[str]] = Field(default_factory=dict)
    child_parents: Dict[str, Set[str]] = Field(default_factory=dict)
