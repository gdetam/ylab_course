"""
hw_03 task_03.

Напишите функцию-декоратор,
которая сохранит (закэширует)
значение декорируемой функции multiplier (Чистая функция).

Если декорируемая функция будет вызвана повторно с теми же параметрами —
декоратор должен вернуть сохранённый результат, не выполняя функцию.

В качестве структуры для кэша, можете использовать словарь в Python.

*В качестве задания со звездочкой
можете использовать вместо Python-словаря => Redis.
"""

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def cached(func):
    cache = {}

    def decorated_func(*args, **kwargs):
        nonlocal cache
        if args in cache:
            logging.info('Data from cache')
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            logging.info('Data added in cache')
            return result

    return decorated_func


@cached
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(2))
    print(multiplier(2))
    print(multiplier(2))
