"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    # в модуле car создайте класс Car
    # класс Car должен быть наследником Vehicle
    # добавьте атрибут engine классу Car
    engine = None

    def set_engine(self, engine: Engine) -> None:
        # объявите метод set_engine, который принимает в себя экземпляр объекта Engine
        # и устанавливает на текущий экземпляр Car
        self.engine = engine
