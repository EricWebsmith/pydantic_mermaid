```mermaid
classDiagram
    class Flavour {
        <<Enumeration>>
        apple: str = 'apple'
        pumpkin: str = 'pumpkin'
        potato: str = 'potato'
    }

    class Pie {
        flavor: Flavour
    }

    class ApplePie {
        flavor: Flavour = 'apple'
    }

    class PumpkinPie {
        flavor: Flavour = 'pumpkin'
    }


    Pie <|-- ApplePie
    Pie <|-- PumpkinPie
```