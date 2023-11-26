```mermaid
classDiagram
    class Male {
        name: str
        age: int
    }

    class Female {
        name: str
        age: int
    }

    class HusbandsRegistry {
        husband_dict: Mapping[Female, Male]
    }

    class WivesRegistry {
        wife_dict: Mapping[Male, Female]
    }


    HusbandsRegistry ..> Male
    HusbandsRegistry ..> Female
    WivesRegistry ..> Male
    WivesRegistry ..> Female

```