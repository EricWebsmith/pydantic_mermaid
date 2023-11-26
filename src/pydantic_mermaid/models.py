from enum import auto, Flag
from typing import Dict, List, Set

from pydantic import BaseModel, Field


__all__ = ["Relations", "MermaidClass", "Property"]


class Relations(Flag):
    """Enum for representing the different types of relationships between classes."""

    Inheritance = auto()
    Dependency = auto()


class Property(BaseModel):
    """A class representing a property of a MermaidClass."""

    name: str
    type: str


class MermaidClass(BaseModel):
    """We call it mermaid class because 'class' is a keyword"""

    name: str
    properties: List[Property]

    def __str__(self) -> str:
        return self.generate_class(set())

    def generate_class(self, exclude: Set[str]) -> str:
        """
        Generate mermaid class definition with some properties omitted.
        This is used when there is a parent class and we want to omit inherited properties.

        :param exclude: A set of property names to be excluded from the generated class definition.
        """
        s = f"\n    class {self.name} {{\n"
        for property in self.properties:
            if property.name in exclude:
                continue
            s += f"        {property.name}: {property.type}\n"
        s += "    }\n"
        return s


class MermaidGraph(BaseModel):
    """A graph of mermaid classes and their relationships"""

    classes: Dict[str, MermaidClass] = Field(default_factory=dict)
    service_clients: Dict[str, Set[str]] = Field(default_factory=dict)
    client_services: Dict[str, Set[str]] = Field(default_factory=dict)
    parent_children: Dict[str, Set[str]] = Field(default_factory=dict)
    child_parents: Dict[str, Set[str]] = Field(default_factory=dict)
