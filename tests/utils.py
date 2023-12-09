from typing import List


# We have normalize and sort the chart because the order of the classes in the chart
# is not deterministic.
def normalize_chart(chart: List[str]) -> List[str]:
    chart = [line.strip() for line in chart if line not in ("", "\n")]
    chart.sort()
    return chart


def compare_charts(actual: List[str], expected: List[str]):
    actual = normalize_chart(actual)
    expected = normalize_chart(expected)
    assert actual == expected
