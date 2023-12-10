from examples import country
from pydantic_mermaid import MermaidGenerator, Relations
from tests.utils import compare_chart_and_markdown


def test_country():
    mg = MermaidGenerator(country)
    chart = mg.generate_chart(root="Country", relations=Relations.Dependency)
    compare_chart_and_markdown(chart, "examples/country_dependency.md")
