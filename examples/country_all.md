```mermaid
classDiagram
    class Place {
        name: str
        population: int
    }

    class County {
    }

    class Region {
        counties: List[County]
    }

    class Province {
        regions: List[Region]
    }

    class City {
        counties: List[County]
    }

    class Country {
        provinces: List[Province]
        cities: List[City]
    }


    Region ..> County
    Province ..> Region
    City ..> County
    Country ..> Province
    Country ..> City

    Place <|-- City
    Place <|-- County
    Place <|-- Country
    Place <|-- Province
    Place <|-- Region
```