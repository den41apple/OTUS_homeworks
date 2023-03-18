"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List


def power_numbers(*numbers) -> List[int]:
    """
    Функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [numb ** 2 for numb in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    """Производит проверку на простое число"""
    if number <= 1:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def filter_numbers(numbers: list, filter_type: str) -> List[int]:
    """
    Функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
