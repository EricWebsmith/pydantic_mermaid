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
    }

    class Cat {
    }

    class Salmon {
    }

    class Eagle {
    }


    Animal <|-- Fish
    Animal <|-- Bird
    Animal <|-- Beast
    Beast <|-- Cat
    Beast <|-- Dog
    Fish <|-- Salmon
    Bird <|-- Eagle
```