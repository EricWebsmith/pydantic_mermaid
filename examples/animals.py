import sys

from pydantic import BaseModel

from pydantic_mermaid import MermaidGenerator


class Animal(BaseModel):
    pass


class Fish(Animal):
    gill = "gill"

    def swim(self):
        pass


class Beast(Animal):
    lags: int

    def run(self):
        pass


class Bird(Animal):
    winds: int

    def fly(self):
        pass


class Dog(Beast):
    pass


class Cat(Beast):
    pass


class Salmon(Fish):
    pass


class Eagle(Bird):
    pass


current_module = sys.modules["__main__"]
mg = MermaidGenerator(current_module)
chart = mg.generate_chart()

with open("./examples/animals.md", mode="w") as f:
    f.write(chart)
    f.close()
