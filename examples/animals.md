```mermaid
classDiagram
    class Animal {
    }

    class Fish {
        gill: str = 'gill'
    }

    class Beast {
        legs: int
    }

    class Bird {
        wings: int
    }

    class Dog {
    }

    class Cat {
    }

    class Salmon {
    }

    class Eagle {
    }


    Animal <|-- Bird
    Animal <|-- Fish
    Animal <|-- Beast
    Beast <|-- Cat
    Beast <|-- Dog
    Fish <|-- Salmon
    Bird <|-- Eagle
```