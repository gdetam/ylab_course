"""
hw_01 task_03.

Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

Будьте осторожны 1000! имеет 2568 цифр.
"""


def zeros(n: int) -> int:
    count: int = 0
    while n >= 5:
        n //= 5
        count += n
    return count


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7

