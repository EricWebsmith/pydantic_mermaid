from copy import deepcopy
from types import ModuleType
from typing import Dict, List, Set, Tuple

from importlib_resources import files
from jinja2 import Environment, FileSystemLoader

from pydantic_mermaid.models import MermaidClass, MermaidGraph, Relations
from pydantic_mermaid.pydantic_parser import PydanticParser

Map = List[Tuple[str, str]]


def render(classes: List[MermaidClass], client_services: Map, parent_children: Map) -> str:
    """Render a mermaid graph to a string"""

    template_path = files("pydantic_mermaid")
    env = Environment(loader=FileSystemLoader(str(template_path)), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("template.j2")
    return template.render(classes=classes, client_services=client_services, parent_children=parent_children)


class MermaidGenerator:
    """genertate a class chart from module"""

    def __init__(self, module: ModuleType) -> None:
        self.graph: MermaidGraph = PydanticParser()(module)
        self.allow_set: Set[str] = set()

    def generate_allow_list(self, root: str, relations: Relations) -> None:
        """
        user can focus on certain class `root` and prune classes that is not inherited from `root`
        or does not depend on `root`
        """
        self.allow_set = {root}
        reversed_class_names = reversed(self.graph.class_names)
        if root != "" and relations & Relations.Dependency:
            for parent in reversed_class_names:
                if parent in self.allow_set and parent in self.graph.service_clients:
                    self.allow_set = self.allow_set | self.graph.service_clients[parent]

        if root != "" and relations & Relations.Inheritance:
            for parent in reversed_class_names:
                if parent in self.allow_set and parent in self.graph.parent_children:
                    self.allow_set = self.allow_set | self.graph.parent_children[parent]

        if root == "":
            self.allow_set = set(self.graph.class_dict)

    def _generate_relationship_map(self, relationship: Dict[str, Set[str]]) -> Map:
        """Generic method to generate relationship maps for dependencies or inheritance."""
        relationship_map: Map = []
        for entity, related_entities in relationship.items():
            if entity not in self.allow_set:
                continue
            for related_entity in related_entities:
                relationship_map.append((entity, related_entity))
        return relationship_map

    def generate_dependencies(self) -> Map:
        """Generate dependencies for class chart using the generic relationship method."""
        return self._generate_relationship_map(self.graph.service_clients)

    def generate_inheritance(self) -> Map:
        """Generate inheritance for class chart using the generic relationship method."""
        return self._generate_relationship_map(self.graph.parent_children)

    def generate_chart(self, *, root: str = "", relations: Relations = Relations.Dependency) -> str:
        """print class chart"""
        self.generate_allow_list(root, relations)

        final_classes: List[MermaidClass] = []

        for class_name in self.allow_set:
            class_value = self.graph.class_dict[class_name]

            final_class = deepcopy(class_value)

            parent_class_name = ""
            if class_name in self.graph.child_parents:
                parent_class_name = next(iter(self.graph.child_parents[class_name]))
            if parent_class_name in self.allow_set and relations != Relations.Dependency:
                inherited_properties = {str(p) for p in self.graph.class_dict[parent_class_name].properties}
                final_class.properties = [p for p in final_class.properties if str(p) not in inherited_properties]

            final_classes.append(final_class)

        client_services: Map = []
        if Relations.Dependency & relations:
            client_services = self.generate_dependencies()

        parent_children: Map = []
        if Relations.Inheritance & relations:
            parent_children = self.generate_inheritance()

        return render(final_classes, client_services, parent_children)
