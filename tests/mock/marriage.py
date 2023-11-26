"""This example is to test dict keys"""
import sys
from typing import Dict

from pydantic import BaseModel
from pydantic_mermaid.mermaid_generator import MermaidGenerator


class Male(BaseModel):
    name: str
    age: int


class Female(BaseModel):
    name: str
    age: int


class HusbandsRegistry(BaseModel):
    husband_dict: Dict[Female, Male]


class WivesRegistry(BaseModel):
    wife_dict: Dict[Male, Female]


if __name__ == "__main__":
    current_module = sys.modules["__main__"]
    mg = MermaidGenerator(current_module)

    chart_dependency = mg.generate_chart()
    with open("tests/mock/marriage.md", mode="w") as f:
        f.write(chart_dependency)
        f.close()
