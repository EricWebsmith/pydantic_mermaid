import sys

from pydantic_mermaid import MermaidGenerator, Relations
from tests.mock.py38 import show_optional

if sys.version_info < (3, 10):
    from types import ModuleType

    import pytest

    from tests.utils import compare_chart_and_markdown

    @pytest.mark.parametrize(
        ("module", "root", "relations", "expected_path"),
        [
            (show_optional, "", Relations.Dependency, "tests/mock/py38/show_optional.md"),
        ],
    )
    def test_gen(module: ModuleType, root: str, relations: Relations, expected_path: str) -> None:
        mg = MermaidGenerator(module)
        chart = mg.generate_chart(root=root, relations=relations)
        compare_chart_and_markdown(chart, expected_path)
