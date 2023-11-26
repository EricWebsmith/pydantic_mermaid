import sys
from typing import List

from pydantic import BaseModel

from pydantic_mermaid import MermaidGenerator, Relations


class Place(BaseModel):
    name: str
    population: int


class County(Place):
    pass


class Region(Place):
    counties: List[County]


class Province(Place):
    regions: List[Region]


class City(Place):
    counties: List[County]


class Country(Place):
    name: str
    provinces: List[Province]
    cities: List[City]


if __name__ == "__main__":
    current_module = sys.modules["__main__"]
    mg = MermaidGenerator(current_module)

    chart_dependency = mg.generate_chart(root="Country")
    with open("./examples/country.md", mode="w") as f:
        f.write(chart_dependency)
        f.close()

    chart_all = mg.generate_chart(relations=Relations.Dependency | Relations.Inheritance)
    with open("./examples/country_all.md", mode="w") as f:
        f.write(chart_all)
        f.close()
