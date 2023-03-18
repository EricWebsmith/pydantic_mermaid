import sys

from pydantic import BaseModel

from pydantic_mermaid.mermaid_generator import MermaidGenerator


class Place(BaseModel):
    name: str
    population: int


class County(Place):
    pass


class Region(Place):
    counties: list[County]


class Province(Place):
    regions: list[Region]


class City(Place):
    counties: list[County]


class Country(Place):
    name: str
    provinces: list[Province]
    cities: list[City]


current_module = sys.modules["__main__"]
mg = MermaidGenerator(current_module)
chart = mg.generate_chart("Country")

with open("./examples/country.md", mode="w") as f:
    f.write(chart)
    f.close()
