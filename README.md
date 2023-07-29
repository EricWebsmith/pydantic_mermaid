# Pydantic Mermaid
To convert Pydantic models to Mermaid charts, you can use the `pydantic-mermaid` library. This library allows you to generate Mermaid charts from your Pydantic models. Here are the steps to install and use pydantic-mermaid:

# Use in terminal

Install the `pydantic-mermaid` library using pip:

```bash
pip install pydantic-mermaid
```

Use command line
```bash
python -m pydantic-mermaid --module models.py --output models.md
```

# Use in code

1. Import your Pydantic models into your Python script.
2. Create an instance of the MermaidGenerator class from the `pydantic-mermaid` module and pass in your Pydantic models as arguments.

```python
from pydantic_mermaid import MermaidGenerator

import my_module

generator = MermaidGenerator(my_module)
```

3. Call the generate_chart() method of the MermaidGenerator instance to generate the Mermaid chart.

```python
chart = generator.generate_chart()
```

4. Use the chart variable to display or save the Mermaid chart.
```python
print(chart)
```

This will print the Mermaid chart as a string. You can also save the chart to a file by writing the chart string to a file:

```python
with open("chart.mmd", "w") as f:
    f.write(chart)
```

This will save the Mermaid chart to a file called chart.mmd. You can then use a tool like the Mermaid Live Editor to visualize and edit the chart.

# examples

Inheritance: 

```mermaid
classDiagram
    class Animal {
    }

    class Fish {
        gill: str
    }

    class Beast {
        lags: int
    }

    class Bird {
        winds: int
    }

    class Dog {
    }

    class Cat {
    }

    class Salmon {
    }

    class Eagle {
    }


    Animal <|-- Fish
    Animal <|-- Bird
    Animal <|-- Beast
    Beast <|-- Cat
    Beast <|-- Dog
    Fish <|-- Salmon
    Bird <|-- Eagle
```

dependencies:

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

For details, check examples/ folder.