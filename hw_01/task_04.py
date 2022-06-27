"""
hw_01 task_04.

Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)

Input: bbananana
"""

import itertools


def bananas(s: str) -> set:
    result: set = set()
    for combination in itertools.combinations(range(len(s)), len(s) - 6):
        words_list: list = list(s)
        for i in combination:
            words_list[i] = '-'
        variant = ''.join(words_list)

        if variant.replace('-', '') == 'banana':
            result.add(variant)
    return result


if __name__ == '__main__':

    assert bananas('banann') == set()
    assert bananas('banana') == {'banana'}

    assert bananas('bbananana') == {'b-an--ana', '-banana--', '-b--anana',
                                    'b-a--nana', '-banan--a', 'b-ana--na',
                                    'b---anana', '-bana--na', '-ba--nana',
                                    'b-anan--a', '-ban--ana', 'b-anana--'}

    assert bananas('bananaaa') == {'banan-a-', 'banana--', 'banan--a'}

    assert bananas('bananana') == {'ban--ana', 'ba--nana', 'bana--na',
                                   'b--anana', 'banana--', 'banan--a'}
