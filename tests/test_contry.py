from examples import country
from pydantic_mermaid import MermaidGenerator, Relations


def test_country():
    mg = MermaidGenerator(country)
    mg.generate_chart(root="Country", relations=Relations.Dependency)
