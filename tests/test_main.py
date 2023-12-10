from pydantic_mermaid import main
from tests.utils import compare_markdowns


def test_main_inheritance(monkeypatch, tmp_path):
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


def test_main_path(monkeypatch, tmp_path):
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


def test_main_country_dependency(monkeypatch, tmp_path):
    file = tmp_path / "country_dependency.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-mermaid",
            "-m",
            "examples.country",
            "-o",
            str(file),
            "-e",
            "dependency",
            "-n",
            "Country",
        ],
    )
    main()

    compare_markdowns(file, "examples/country_dependency.md")


def test_main_both_inheritance_dependency(monkeypatch, tmp_path):
    file = tmp_path / "animals.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-mermaid",
            "-m",
            "examples.country",
            "-o",
            str(file),
            "-e",
            "inheritance",
            "dependency",
        ],
    )
    main()

    compare_markdowns(file, "examples/country_all.md")
