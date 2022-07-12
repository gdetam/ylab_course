"""
hw_03 task_04.

Надо написать декоратор для повторного выполнения
декорируемой функции через некоторое время.

Использует наивный экспоненциальный рост времени повтора (factor)
до граничного времени ожидания (border_sleep_time).

В качестве параметров декоратор будет получать:

call_count - число, описывающее кол-во раз запуска функций;
start_sleep_time - начальное время повтора;
factor - во сколько раз нужно увеличить время ожидания;
border_sleep_time - граничное время ожидания.
Формула:

t = start_sleep_time * 2^(n) if t < border_sleep_time
t = border_sleep_time if t >= border_sleep_time
"""

from time import sleep


def repeat_decorator(call_count=None, start_sleep_time=None,
                     factor=None, border_sleep_time=None):

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Кол-во запусков = {call_count}\nНачало работы')
            t = start_sleep_time
            for i in range(1, call_count + 1):
                sleep(t)
                if t < border_sleep_time:
                    t = start_sleep_time * factor**i
                else:
                    t = border_sleep_time
                print(
                    f'Запуск номер {i}. '
                    f'Ожидание: {t} секунд. '
                    f'Результат декорируемой функций = '
                    f'{func(*args, **kwargs)}.'
                )
            print('Конец работы')

        return wrapper

    return decorator


@repeat_decorator(call_count=3, start_sleep_time=1,
                  factor=2, border_sleep_time=10)
def multiplier(n):
    return n * 2


if __name__ == '__main__':
    multiplier(2)
