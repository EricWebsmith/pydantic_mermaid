from pydantic_mermaid import MermaidGenerator, Relations
from tests.mock import cat_dog_shop
from tests.utils import compare_chart_and_markdown


def test_cat_and_dogs() -> None:
    mg = MermaidGenerator(cat_dog_shop)
    chart = mg.generate_chart(relations=Relations.Dependency)
    compare_chart_and_markdown(chart, "tests/mock/cat_and_dogs.md")
