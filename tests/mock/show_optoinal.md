```mermaid
classDiagram

    class Person {
        name: Optional[str] = None
        nick_name: Optional[str] = None
        full_name: str = get_name
        age: Optional[int] = None
        friends: List[str] = list
        families: List[str] = list
        city: str
        addr: str = ''
    }



```