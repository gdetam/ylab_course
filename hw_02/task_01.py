"""
hw_02 task_01.

Разработать программу для вычисления кратчайшего пути для почтальона.

Описание задачи:
Почтальон выходит из почтового отделения,
объезжает всех адресатов один раз для вручения посылки
и возвращается в почтовое отделение.

Необходимо найти кратчайший маршрут для почтальона.

Координаты точек:
1) Почтовое отделение – (0, 2)
2) Ул. Грибоедова, 104/25 – (2, 5)
3) Ул. Бейкер стрит, 221б – (5, 2)
4) Ул. Большая Садовая, 302-бис – (6, 6)
5) Вечнозелёная Аллея, 742 – (8, 3)
"""


def distance_calc(x1: int, y1: int, x2: int, y2: int) -> float:
    """Calculates distance between two points"""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def full_path_calc(locations: list) -> int:
    """Calculates full path distance"""
    res = 0

    for i in range(len(locations) - 1):
        res += distance_calc(*locations[i], *locations[i + 1])

    return res


def postman_path_print(locations: list):
    """Prints full path and distance between points"""
    res = 0
    distances = []

    for i in range(len(locations) - 1):
        res += distance_calc(*locations[i], *locations[i + 1])
        distances.append(res)

    print(
        f'{locations[0]} -> '
        f'{locations[1]}[{distances[0]}] -> '
        f'{locations[2]}[{distances[1]}] -> '
        f'{locations[3]}[{distances[2]}] -> '
        f'{locations[4]}[{distances[3]}] -> '
        f'{locations[5]}[{distances[4]}] = {distances[4]}')


def postman(start: tuple, locations: list):
    """Locates the best path for postman"""
    locations_list = []
    result_distance = -1
    for i in range(0, 4):
        j_copy = locations[:i] + locations[i + 1:]
        for j in range(len(j_copy)):
            k_copy = j_copy[:j] + j_copy[j + 1:]
            for k in range(len(k_copy)):

                compare_list = [start, locations[i],
                                j_copy[j], k_copy[k],
                                k_copy[1 - k], start]

                compare_distance = full_path_calc(compare_list)
                if result_distance == -1 or compare_distance < result_distance:
                    locations_list = compare_list[:]
                    result_distance = compare_distance
    postman_path_print(locations_list)


# location points
post_office = (0, 2)
griboedova = (2, 5)
beyker_street = (5, 2)
bolshaya_sadovaya = (6, 6)
vechno_zelenaya_alleya = (8, 3)

postman(post_office, [griboedova, beyker_street,
                      bolshaya_sadovaya, vechno_zelenaya_alleya])
