from examples import animals
from pydantic_mermaid import MermaidGenerator, Relations
from tests.utils import compare_chart_and_markdown


def test_animals():
    mg = MermaidGenerator(animals)
    chart = mg.generate_chart(relations=Relations.Inheritance)
    compare_chart_and_markdown(chart, "examples/animals.md")


def test_animals_brids():
    mg = MermaidGenerator(animals)
    chart = mg.generate_chart(root="Bird", relations=Relations.Inheritance)
    compare_chart_and_markdown(chart, "examples/animals_birds.md")
