from pathlib import Path
from typing import List, Union


# We have normalize and sort the chart because the order of the classes in the chart
# is not deterministic.
def normalize_chart(chart: List[str]) -> List[str]:
    chart = [line.strip() for line in chart if line not in ("", "\n")]
    chart.sort()
    return chart


def compare_charts(actual: List[str], expected: List[str]) -> None:
    actual = normalize_chart(actual)
    expected = normalize_chart(expected)
    assert actual == expected


def compare_chart_and_markdown(chart: str, markdown_path: str) -> None:
    markdown_path = Path(markdown_path)
    markdown_path_actual = Path(markdown_path).parent / f"{markdown_path.stem}-actual{markdown_path.suffix}"
    with markdown_path_actual.open("w") as f:
        f.write(chart)

    compare_markdowns(str(markdown_path_actual), str(markdown_path))


def compare_markdowns(markdown_path_1: Union[str, Path], markdown_path_2: Union[str, Path]) -> None:
    chart_1_lines = []
    with Path(markdown_path_1).open(mode="r") as f:
        chart_1_lines = f.readlines()

    chart_1_lines.sort()

    chart_2_lines = []
    with Path(markdown_path_2).open(mode="r") as f:
        chart_2_lines = f.readlines()

    chart_2_lines.sort()

    compare_charts(chart_1_lines, chart_2_lines)
