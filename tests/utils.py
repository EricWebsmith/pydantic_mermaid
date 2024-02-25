from __future__ import annotations

from pathlib import Path
from re import Pattern, compile
from typing import List, Tuple, Union

type_keyword_re: List[Tuple[Pattern[str], str]] = [
    (compile(r"\btuple\b"), "Tuple"),
    (compile(r"\blist\b"), "List"),
    (compile(r"\bdict\b"), "Dict"),
    (compile(r"\bset\b"), "Set"),
]


def normalize_line(line: str) -> str:
    """Normalize a line by stripping leading and trailing whitespace and ignore type case."""
    line = line.strip()
    for pattern, replacement in type_keyword_re:
        line = pattern.sub(replacement, line)
    return line


def normalize_chart(chart: List[str]) -> List[str]:
    """Normalize and sort the chart because the order of the classes in the chart is not deterministic."""
    chart = [normalize_line(line) for line in chart if line not in ("", "\n")]
    chart.sort()
    return chart


def compare_charts(actual: List[str], expected: List[str]) -> None:
    actual = normalize_chart(actual)
    expected = normalize_chart(expected)
    assert actual == expected


def compare_chart_and_markdown(chart: str, markdown_path: Union[str, Path]) -> None:
    markdown_path = Path(markdown_path)
    markdown_path_actual = Path(markdown_path).parent / f"{markdown_path.stem}-actual{markdown_path.suffix}"
    with markdown_path_actual.open("w") as f:
        f.write(chart)

    actual = chart.split("\n")
    actual.sort()

    expected = []
    with markdown_path.open(mode="r") as f:
        expected = f.readlines()

    expected.sort()

    compare_charts(actual, expected)


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
