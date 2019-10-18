"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def quiz_borndate(name_genitive, bornyear, birthday):
    year = input(f'Введите год рождения {name_genitive}: ')
    while year != bornyear:
        print(f"Нет, не {year}-й")
        year = input(f'Введите год рождения {name_genitive}: ')
    print(f'Верно, {bornyear}-й год')

    day = input(f'Введите день рождения {name_genitive}: ')
    while day != birthday:
        print(f"Нет, не {day}-го")
        day = input(f'Введите день рождения {name_genitive}: ')
    print(f'Верно, {birthday}-го числа')

quiz_borndate('А.С.Пушкина', '1799', '6')
quiz_borndate('Уильяма Шекспира', '1564', '1')