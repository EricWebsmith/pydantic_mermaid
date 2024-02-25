from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


def get_name() -> str:
    return "name"


class Person(BaseModel):
    name: Optional[str] = None
    full_name: str = Field(title="Full Name", description="Full name of the person", default_factory=get_name)
    age: Optional[int] = Field(None, title="Age", description="Age of the person")
    friends: List[str] = Field(title="Friends", description="List of friends", default_factory=list)
    city: str
    addr: str = ""
