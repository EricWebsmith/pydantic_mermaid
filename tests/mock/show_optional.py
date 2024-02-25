from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


def get_name() -> str:
    return "name"


class Person(BaseModel):
    name: Optional[str] = Field(None, title="Name", description="Name of the person")
    nick_name: str | None = None
    full_name: str = Field(title="Full Name", description="Full name of the person", default_factory=get_name)
    age: Optional[int] = Field(None, title="Age", description="Age of the person")
    friends: List[str] = Field(title="Friends", description="List of friends", default_factory=list)
    families: list[str] = Field(title="Families", description="List of families", default_factory=list)
    city: str
    addr: str = ""
