from enum import Enum

from pydantic import BaseModel


class Flavour(str, Enum):
    APPLE = "apple"
    PUMPKIN = "pumpkin"
    POTATO = "potato"


class Pie(BaseModel):
    flavor: Flavour


class ApplePie(Pie):
    flavor: Flavour = Flavour.APPLE


class PumpkinPie(Pie):
    flavor: Flavour = Flavour.POTATO
