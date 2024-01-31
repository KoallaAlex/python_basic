# """
# Домашнее задание №1
# Функции и структуры данных
# """
from typing import List


def power_numbers(*numbers_list, power=2):
    return [number ** power for number in numbers_list]
    # """
    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]
    # """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

    prime_numbers = list(filter(is_prime, numbers_list))



def filter_numbers(numbers_list, filter_types):
    if filter_types == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    if filter_types == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    if filter_types == PRIME:
        return

# Не знаю как модифоцироать функцию чтобы она прошла тест!!!! Помогите, пожалуйста!

    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """
