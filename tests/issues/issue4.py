"""
https://github.com/EricWebsmith/pydantic-2-mermaid/issues/4
"""

from typing import Tuple

from pydantic import BaseModel, Field


class Variable(BaseModel):
    name: str = Field(...)
    value: float = Field(...)


class Data(BaseModel):
    variables: Tuple[Variable, ...] = Field(...)
