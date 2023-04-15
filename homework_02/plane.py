"""
создайте класс `Plane`, наследник `Vehicle`
"""
from typing import Union

from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    # в модуле plane создайте класс Plane
    # класс Plane должен быть наследником Vehicle
    # добавьте атрибуты cargo и max_cargo классу Plane
    cargo = 0
    max_cargo = None

    def __init__(self, weight: Union[int, float], fuel: Union[int, float],
                 fuel_consumption: Union[int, float], max_cargo: Union[int, float]):
        # добавьте max_cargo в инициализатор (переопределите родительский)
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, additional_cargo: Union[int, float]) -> Union[int, float]:
        # объявите метод load_cargo, который принимает число,
        # проверяет, что в сумме с текущим cargo не будет перегруза,
        # и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
        cargo_total = additional_cargo + self.cargo
        if cargo_total > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo = cargo_total
            return self.cargo

    def remove_all_cargo(self) -> Union[int, float]:
        old_cargo = self.cargo  # Старое значение cargo
        # объявите метод remove_all_cargo, который обнуляет значение cargo
        self.cargo = 0
        # и возвращает значение cargo, которое было до обнуления
        return old_cargo
