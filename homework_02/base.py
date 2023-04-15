from abc import ABC
from typing import Union

from .exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    weight = 1_000
    started = False
    fuel = 0
    fuel_consumption = 9

    def __init__(self, weight: Union[int, float], fuel: Union[int, float], fuel_consumption: Union[int, float]):
        # добавьте инициализатор для установки weight, fuel, fuel_consumption
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None:
        # добавьте метод start, который, если ещё не состояние started,
        # проверяет, что топлива больше нуля
        # и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
        if self.started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: Union[int, float]) -> None:
        # добавьте метод move, который проверяет,
        # что достаточно топлива для преодоления переданной дистанции,
        # и изменяет количество оставшегося топлива,
        # иначе выкидывает исключение exceptions.NotEnoughFuel

        fuel_required = self.fuel_consumption * distance  # Требуемое кол-во топлива для преодоления пути
        if fuel_required <= self.fuel:
            self.fuel -= fuel_required
        else:
            raise NotEnoughFuel
