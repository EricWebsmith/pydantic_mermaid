from pathlib import Path

from examples import animals
from pydantic_mermaid import MermaidGenerator, Relations
from tests.utils import compare_charts


def test_animals():
    mg = MermaidGenerator(animals)
    chart = mg.generate_chart(relations=Relations.Inheritance)
    actual = chart.split("\n")

    expected = []
    with Path("./examples/animals.md").open(mode="r") as f:
        expected = f.readlines()

    compare_charts(actual, expected)


def test_animals_brids():
    mg = MermaidGenerator(animals)
    chart = mg.generate_chart(root="Bird", relations=Relations.Inheritance)
    actual = chart.split("\n")

    expected = []
    with Path("./examples/animals_birds.md").open(mode="r") as f:
        expected = f.readlines()

    compare_charts(actual, expected)
