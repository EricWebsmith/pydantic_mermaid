# Pydantic Mermaid

[![CI](https://github.com/ericwebsmith/pydantic_mermaid/workflows/CI/badge.svg)](https://github.com/EricWebsmith/pydantic_mermaid/actions/workflows/ci.yml)
![Coverage](https://codecov.io/gh/ericwebsmith/pydantic_mermaid/branch/main/graph/badge.svg)
[![pypi](https://img.shields.io/pypi/v/pydantic_mermaid.svg)](https://pypi.python.org/pypi/pydantic_mermaid)
[![downloads](https://static.pepy.tech/badge/pydantic_mermaid/month)](https://pepy.tech/project/pydantic_mermaid)
[![versions](https://img.shields.io/pypi/pyversions/pydantic_mermaid.svg)](https://github.com/ericwebsmith/pydantic_mermaid)
[![license](https://img.shields.io/github/license/ericwebsmith/pydantic_mermaid.svg)](https://github.com/ericwebsmith/pydantic_mermaid/blob/main/LICENSE)

To convert Pydantic models to Mermaid charts, you can use the `pydantic-mermaid` library. This library allows you to generate Mermaid charts from your Pydantic models. Here are the steps to install and use pydantic-mermaid:

If you are using pydantic 2, please visit [https://github.com/EricWebsmith/pydantic-2-mermaid](https://github.com/EricWebsmith/pydantic-2-mermaid)

# Use in terminal

Install the `pydantic-mermaid` library using pip:

```bash
pip install pydantic-mermaid
```

Use command line
```bash
pydantic-mermaid --module models.py --output models.md
```

You can run the following comamand get help for the command.
```bash
pydantic-mermaid --help
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

**Administrative Divisions of the United States of America**

```mermaid
classDiagram
    class Municipality {
        name: str
        population: int
    }

    class MinorCivilDivision {
        name: str
        population: int
    }

    class County {
        name: str
        population: int
        municipalities: list[Municipality]
        minor_civil_divisions: list[MinorCivilDivision]
    }

    class CountyEquivalant {
        name: str
        population: int
    }

    class State {
        name: str
        population: int
        counties: list[County]
        county_equivalants: list[CountyEquivalant]
    }

    class FederalDistrict {
        name: str
        population: int
    }

    class InhabitedTerritory {
        name: str
        population: int
    }

    class HabitedTerritory {
        name: str
        population: int
    }

    class Federal {
        name: str
        population: int
        federal_distric: FederalDistrict
        states: list[State]
        Inhabited_territories: list[InhabitedTerritory]
        Habited_territories: list[HabitedTerritory]
    }


    County ..> MinorCivilDivision
    County ..> Municipality
    State ..> CountyEquivalant
    State ..> County
    Federal ..> InhabitedTerritory
    Federal ..> HabitedTerritory
    Federal ..> State
    Federal ..> FederalDistrict

```

For details, check examples/ folder.