import random
import datetime
from math import floor
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, name: str, model: str, year: int, color: str, wheels: int, seats: int, market_value: float) -> object:

        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.wheels = wheels
        self.seats = seats
        self.market_value = market_value

    # DUNDER METHODS
    def __str__(self):
        return f'{self.name},{self.model},{self.year},{self.color}'

    # METHODS
    def MVET(self, mvte_tax=25) -> float:
        return(Vehicle.mvte_rate(self.market_value, mvte_tax))

    def age(self) -> int:
        return(datetime.datetime.now().year - self.year)

    # STATIC METHODS
    @staticmethod
    def mvte_rate(vehicle_value, tax):
        return round((vehicle_value/1000)*tax, 2)
