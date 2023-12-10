from pydantic_mermaid import MermaidGenerator, Relations
from tests.mock import marriage
from tests.utils import compare_chart_and_markdown


def test_marriage():
    mg = MermaidGenerator(marriage)
    chart = mg.generate_chart(relations=Relations.Dependency)
    compare_chart_and_markdown(chart, "tests/mock/marriage.md")
