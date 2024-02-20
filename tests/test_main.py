from pathlib import Path

import pytest

from pydantic_mermaid import main
from tests.utils import compare_markdowns


def test_main_inheritance(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    file = tmp_path / "animals.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-mermaid",
            "-m",
            "examples.animals",
            "-o",
            str(file),
            "-e",
            "inheritance",
        ],
    )
    main()

    compare_markdowns(file, "examples/animals.md")


def test_main_path(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    file = tmp_path / "animals.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-mermaid",
            "-m",
            "./examples/animals.py",
            "-o",
            str(file),
            "-e",
            "inheritance",
        ],
    )
    main()

    compare_markdowns(file, "examples/animals.md")


def test_main_usa_dependency(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    file = tmp_path / "usa_dependency.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-mermaid",
            "-m",
            "examples.usa",
            "-o",
            str(file),
            "-e",
            "dependency",
            "-n",
            "Federal",
        ],
    )
    main()

    compare_markdowns(file, "examples/usa_dependency.md")


def test_main_both_inheritance_dependency(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    file = tmp_path / "animals.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-mermaid",
            "-m",
            "examples.usa",
            "-o",
            str(file),
            "-e",
            "both",
        ],
    )
    main()

    compare_markdowns(file, "examples/usa_both.md")
