from types import ModuleType

import pytest

from examples import animals, usa
from pydantic_mermaid import MermaidGenerator, Relations
from tests.issues import issue4
from tests.mock import cat_dog_shop, enum_example, marriage
from tests.utils import compare_chart_and_markdown


@pytest.mark.parametrize(
    ("module", "root", "relations", "expected_path"),
    [
        (animals, "", Relations.Inheritance, "examples/animals.md"),
        (animals, "Bird", Relations.Inheritance, "examples/animals_birds.md"),
        (cat_dog_shop, "", Relations.Dependency, "tests/mock/cat_and_dogs.md"),
        (enum_example, "", Relations.Inheritance, "tests/mock/enum_example.md"),
        (marriage, "", Relations.Dependency, "tests/mock/marriage.md"),
        (usa, "Federal", Relations.Dependency, "examples/usa_dependency.md"),
        (issue4, "", Relations.Dependency, "tests/issues/issue4.md"),
    ],
)
def test_animals(module: ModuleType, root: str, relations: Relations, expected_path: str) -> None:
    mg = MermaidGenerator(module)
    chart = mg.generate_chart(root=root, relations=relations)
    compare_chart_and_markdown(chart, expected_path)
