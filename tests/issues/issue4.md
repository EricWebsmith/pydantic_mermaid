```mermaid
classDiagram

    class Variable {
        name: str
        value: float
    }

    class Data {
        variables: tuple[Variable, ...]
    }

    Data ..> Variable


```