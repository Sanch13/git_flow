from typing import NamedTuple
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    lon: float
    lat: float


def get_coordinates() -> Coordinates:

    return Coordinates(lon=10.0, lat=20.2)


