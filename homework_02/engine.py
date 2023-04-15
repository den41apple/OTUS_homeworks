"""
create dataclass `Engine`
"""
from dataclasses import dataclass
from typing import Union


@dataclass
class Engine:
    # создайте датакласс Engine в модуле engine, добавьте атрибуты volume и pistons
    volume: Union[int, float]
    pistons: Union[int, float]

    def __init__(self, volume, pistons):
        # -- В задании этого нет, но судя по тестам, здесь нужен инициализатор --
        self.volume = volume
        self.pistons = pistons
