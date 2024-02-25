import sys

if sys.version_info >= (3, 10):
    from pydantic import BaseModel, Field

    def get_name() -> str:
        return "name"

    class Person(BaseModel):
        name: str | None = None
        full_name: str = Field(title="Full Name", description="Full name of the person", default_factory=get_name)
        age: int | None = None
        friends: list[str] = Field(title="Friends", description="List of friends", default_factory=list)
        city: str
        addr: str = ""
