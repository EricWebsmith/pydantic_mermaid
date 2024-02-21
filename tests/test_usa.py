from examples import usa
from pydantic_mermaid import MermaidGenerator, Relations
from tests.utils import compare_chart_and_markdown


def test_usa() -> None:
    mg = MermaidGenerator(usa)
    chart = mg.generate_chart(root="Federal", relations=Relations.Dependency)
    compare_chart_and_markdown(chart, "examples/usa_dependency.md")
