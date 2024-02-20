from enum import Enum

from pydantic import BaseModel


class Flavour(str, Enum):
    apple = "apple"
    pumpkin = "pumpkin"
    potato = "potato"


class Pie(BaseModel):
    flavor: Flavour


class ApplePie(Pie):
    flavor: Flavour = Flavour.apple  # type: ignore


class PumpkinPie(Pie):
    flavor: Flavour = Flavour.pumpkin  # type: ignore
