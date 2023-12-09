from pydantic_mermaid import main


def test_main(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["pydantic-2-mermaid", "-m", "examples.animals", "-o", "./examples/animals.tmp.md", "-e", "inheritance"],
    )
    main()


def test_main_path(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "pydantic-2-mermaid",
            "-m",
            "./examples/animals.py",
            "-o",
            "./examples/animals.path.tmp.md",
            "-e",
            "inheritance",
        ],
    )
    main()
