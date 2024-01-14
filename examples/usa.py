import sys
from pathlib import Path
from typing import List

from pydantic import BaseModel

from pydantic_mermaid import MermaidGenerator, Relations


class AdministrativeDivision(BaseModel):
    name: str
    population: int


class Municipality(AdministrativeDivision):
    pass


class MinorCivilDivision(AdministrativeDivision):
    pass


class County(AdministrativeDivision):
    municipalities: List[Municipality]
    minor_civil_divisions: List[MinorCivilDivision]


class CountyEquivalant(AdministrativeDivision):
    pass


class State(AdministrativeDivision):
    counties: List[County]
    county_equivalants: List[CountyEquivalant]


class FederalDistrict(AdministrativeDivision):
    """
    There is on ferderal district in the USA. It is Washington, D.C.,
    formally the District of Columbia and commonly called Washington or D.C
    """

    pass


class InhabitedTerritory(AdministrativeDivision):
    pass


class HabitedTerritory(AdministrativeDivision):
    pass


class Federal(AdministrativeDivision):
    federal_distric: FederalDistrict
    states: List[State]
    Inhabited_territories: List[InhabitedTerritory]
    Habited_territories: List[HabitedTerritory]


if __name__ == "__main__":
    current_module = sys.modules["__main__"]
    mg = MermaidGenerator(current_module)

    chart_dependency = mg.generate_chart(relations=Relations.Inheritance)
    with Path("./examples/usa_inheritance.md").open(mode="w") as f:
        f.write(chart_dependency)

    chart_dependency = mg.generate_chart(root="Federal", relations=Relations.Dependency)
    with Path("./examples/usa_dependency.md").open(mode="w") as f:
        f.write(chart_dependency)

    chart_both = mg.generate_chart(relations=Relations.Dependency | Relations.Inheritance)
    with Path("./examples/usa_both.md").open(mode="w") as f:
        f.write(chart_both)
        f.close()


# CLI
"""
pydantic-mermaid -m examples.usa -o examples/usa_inheritance.md -e inheritance
pydantic-mermaid -m examples.usa -o examples/usa_dependency.md -e dependency -n Federal
pydantic-mermaid -m examples.usa -o examples/usa_both.md -e both -n Federal
"""
