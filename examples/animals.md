```mermaid
classDiagram
    class Animal {
    }

    class Fish {
        gill: str
    }

    class Beast {
        lags: int
    }

    class Bird {
        winds: int
    }

    class Dog {
        lags: int
    }

    class Cat {
        lags: int
    }

    class Salmon {
        gill: str
    }

    class Eagle {
        winds: int
    }



    Animal <|-- Beast
    Animal <|-- Bird
    Animal <|-- Fish
    Beast <|-- Dog
    Beast <|-- Cat
    Fish <|-- Salmon
    Bird <|-- Eagle
```