"""
@file
@brief Ро-метод факторизации Полларда
"""


def algorithm():
    """"
    @brief Решает задачу дискретного логарифмирования для заданного сравнения
    @param a Основание степени
    @param b Остаток взятия по модулю
    @param p Модуль сравнения
    @param table Все итерации
    @return Решение сравнения
    """
    a = 15
    b = 4
    p = 31
    x = 0

    ui = 0
    vi = 0
    zi = 0
    t = True

    table = [[0, 0, 1]]

    while t:
        if zi * 3 < p:
            ui += 1
        elif zi * 3 > 2 * p:
            vi += 1
        elif (3 * zi > p) and (3 * zi < 2 * p):
            ui *= 2
            vi *= 2
        zi = ((a ** ui) * (b ** vi)) % p
        table.append([ui, vi, zi])
        for i in range(0, len(table) - 2):
            if table[i][2] == zi:
                t = False
                x = ((table[i][0] - ui) / (vi - table[i][1])) % (p - 1)
    if x < 0:
        x += p
    print (x)

