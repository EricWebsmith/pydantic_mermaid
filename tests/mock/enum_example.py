from enum import Enum

from pydantic import BaseModel


class Flaver(str, Enum):
    apple = "apple"
    pumpkin = "pumpkin"


class AppleFlaver(str, Enum):
    apple = "apple"


class PumpkinFlaver(str, Enum):
    pumpkin = "pumpkin"


class Pie(BaseModel):
    flavor: Flaver


class ApplePie(Pie):
    flavor: AppleFlaver  # type: ignore


class PumpkinPie(Pie):
    flavor: PumpkinFlaver  # type: ignore
