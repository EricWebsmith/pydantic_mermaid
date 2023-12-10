```mermaid
classDiagram
    class Municipality {
        name: str
        population: int
    }

    class MinorCivilDivision {
        name: str
        population: int
    }

    class County {
        name: str
        population: int
        municipalities: List[Municipality]
        minor_civil_divisions: List[MinorCivilDivision]
    }

    class CountyEquivalant {
        name: str
        population: int
    }

    class State {
        name: str
        population: int
        counties: List[County]
        county_equivalants: List[CountyEquivalant]
    }

    class FederalDistrict {
        name: str
        population: int
    }

    class InhabitedTerritory {
        name: str
        population: int
    }

    class HabitedTerritory {
        name: str
        population: int
    }

    class Federal {
        name: str
        population: int
        federal_distric: FederalDistrict
        states: List[State]
        Inhabited_territories: List[InhabitedTerritory]
        Habited_territories: List[HabitedTerritory]
    }


    County ..> Municipality
    County ..> MinorCivilDivision
    State ..> CountyEquivalant
    State ..> County
    Federal ..> FederalDistrict
    Federal ..> State
    Federal ..> InhabitedTerritory
    Federal ..> HabitedTerritory

```