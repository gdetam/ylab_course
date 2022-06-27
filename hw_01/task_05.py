"""
hw_01 task_05.

Написать метод count_find_num,
который принимает на вход список простых множителей
(primesL) и целое число, предел (limit),
после чего попробуйте сгенерировать по порядку все числа.

Меньшие значения предела, которые имеют все
и только простые множители простых чисел primesL.
"""

import math


def count_find_num(primesL: list, limit: int) -> list:
    all_values: list = []
    total = math.prod(primesL)
    all_values.append(total)
    if total > limit:
        return []

    for num in primesL:
        for total in all_values:
            value = num * total
            if value <= limit and value not in all_values:
                all_values.append(value)

    return [len(all_values), max(all_values)]


if __name__ == '__main__':

    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
