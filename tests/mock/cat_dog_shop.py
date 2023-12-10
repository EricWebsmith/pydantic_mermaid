import sys
from pathlib import Path
from typing import List, Union

from pydantic import BaseModel

from pydantic_mermaid import MermaidGenerator, Relations


class Cat(BaseModel):
    name: str
    age: int


class Dog(BaseModel):
    name: str
    age: int


class Shop(BaseModel):
    cat_and_dogs: List[Union[Cat, Dog]]


if __name__ == "__main__":
    current_module = sys.modules["__main__"]
    mg = MermaidGenerator(current_module)
    chart = mg.generate_chart(relations=Relations.Dependency)

    with Path("tests/mock/cat_and_dogs.md").open(mode="w") as f:
        f.write(chart)
        f.close()
