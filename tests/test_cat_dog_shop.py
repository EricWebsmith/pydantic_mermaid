from pydantic_mermaid import MermaidGenerator, Relations
from tests.mock import cat_dog_shop
from tests.utils import compare_charts


def test_cat_and_dogs():
    mg = MermaidGenerator(cat_dog_shop)
    chart = mg.generate_chart(relations=Relations.Dependency)
    actual = chart.split("\n")

    expected = []
    with open("tests/mock/cat_and_dogs.md", mode="r") as f:
        expected = f.readlines()

    compare_charts(actual, expected)
