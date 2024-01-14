```mermaid
classDiagram
    class Pie {
        flavor: Flaver
    }

    class ApplePie {
        flavor: AppleFlaver
    }

    class PumpkinPie {
        flavor: PumpkinFlaver
    }


    Pie <|-- ApplePie
    Pie <|-- PumpkinPie
```