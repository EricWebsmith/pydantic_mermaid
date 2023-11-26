from pydantic_mermaid import MermaidGenerator, Relations
from tests.mock import marriage
from tests.utils import compare_charts


def test_marriage():
    mg = MermaidGenerator(marriage)
    chart = mg.generate_chart(relations=Relations.Dependency)
    actual = chart.split("\n")

    expected = []
    with open("tests/mock/marriage.md", mode="r") as f:
        expected = f.readlines()

    compare_charts(actual, expected)
