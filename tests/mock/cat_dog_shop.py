from typing import List, Union

from pydantic import BaseModel


class Cat(BaseModel):
    name: str
    age: int


class Dog(BaseModel):
    name: str
    age: int


class Shop(BaseModel):
    cat_and_dogs: List[Union[Cat, Dog]]
