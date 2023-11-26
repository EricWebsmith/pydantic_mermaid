from types import ModuleType
from typing import Set

from pydantic_mermaid.models import MermaidGraph, Relations
from pydantic_mermaid.pydantic_parser import PydanticParser


class MermaidGenerator:
    """genertate a class chart from module"""

    def __init__(self, module: ModuleType) -> None:
        self.g: MermaidGraph = PydanticParser()(module)
        self.allow_set: Set[str] = set()

    def generate_allow_list(self, root: str, relations: Relations) -> None:
        """
        user can focus on certain class `root` and prune classes that is inherited from `root`
        or not a dependencies of `root`
        """
        self.allow_set = {root}
        if root != "" and relations & Relations.Dependency:
            parents = list(self.g.service_clients.keys())
            parents.reverse()
            for parent in parents:
                if parent in self.allow_set:
                    self.allow_set = self.allow_set | self.g.service_clients[parent]

        if root != "" and relations & Relations.Inheritance:
            parents = list(self.g.parent_children.keys())
            parents.reverse()
            for parent in parents:
                if parent in self.allow_set:
                    self.allow_set = self.allow_set | self.g.parent_children[parent]

        if root == "":
            self.allow_set = {class_name for class_name in self.g.classes}

    def generate_dependencies(self) -> str:
        """print dependencies for class chart"""
        s = ""
        for dependant, depended in self.g.service_clients.items():
            if dependant not in self.allow_set:
                continue

            for d in depended:
                if d not in self.allow_set:
                    continue
                s += f"    {dependant} ..> {d}\n"

        s += "\n"
        return s

    def generate_inheritance(self) -> str:
        """print inheritance for class chart"""
        s = ""
        for parent, children in self.g.parent_children.items():
            if parent not in self.allow_set:
                continue
            for child in children:
                if child not in self.allow_set:
                    continue
                s += f"    {parent} <|-- {child}\n"
        return s

    def generate_chart(self, *, root: str = "", relations: Relations = Relations.Dependency) -> str:
        """print class chart"""
        self.generate_allow_list(root, relations)

        s = "```mermaid\nclassDiagram"
        for class_name, class_type in self.g.classes.items():
            if class_name not in self.allow_set:
                continue

            parent_class_name = ""
            if class_name in self.g.child_parents:
                parent_class_name = list(self.g.child_parents[class_name])[0]
            if parent_class_name in self.allow_set:
                inherited_properties = {p.name for p in self.g.classes[parent_class_name].properties}
                s += class_type.generate_class(exclude=inherited_properties)
            else:
                s += str(class_type)

        s += "\n\n"

        if Relations.Dependency in relations:
            s += self.generate_dependencies()

        if Relations.Inheritance in relations:
            s += self.generate_inheritance()

        s += "```"
        return s
