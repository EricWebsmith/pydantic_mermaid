from pydantic_mermaid import MermaidGenerator, Relations
from tests.mock import enum_example
from tests.utils import compare_chart_and_markdown


def test_animals_brids():
    mg = MermaidGenerator(enum_example)
    chart = mg.generate_chart(relations=Relations.Inheritance)
    compare_chart_and_markdown(chart, "tests/mock/enum_example.md")
