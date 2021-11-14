# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water():

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if str(other) == 'Воздух':
            new_obj = f'{self} + {other} = {Storm()}'
            return new_obj
        elif str(other) == 'Огонь':
            new_obj = f'{self} + {other} = {Steam()}'
            return new_obj
        elif str(other) == 'Земля':
            new_obj = f'{self} + {other} = {Dirt()}'
            return new_obj
        elif str(other) == 'Лава':
            new_obj = f'{self} + {other} = {Obsidian()}'
            return new_obj
        else:
            return None

class Air():
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if str(other) == 'Вода':
            new_obj = f'{self} + {other} = {Storm()}'
            return new_obj
        elif str(other) == 'Огонь':
            new_obj = f'{self} + {other} = {Lighting()}'
            return new_obj
        elif str(other) == 'Земля':
            new_obj = f'{self} + {other} = {Dust()}'
            return new_obj
        else:
            return None

class Fire():
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if str(other) == 'Воздух':
            new_obj = f'{self} + {other} = {Lighting()}'
            return new_obj
        elif str(other) == 'Вода':
            new_obj = f'{self} + {other} = {Steam()}'
            return new_obj
        elif str(other) == 'Земля':
            new_obj = f'{self} + {other} = {Lava()}'
            return new_obj
        else:
            return None
class Earth():
    def __str__(self):
        return 'Земля'
    def __add__(self, other):
        if str(other) == 'Вода':
            new_obj = f'{self} + {other} = {Dirt()}'
            return new_obj
        elif str(other) == 'Огонь':
            new_obj = f'{self} + {other} = {Lava()}'
            return new_obj
        elif str(other) == 'Воздух':
            new_obj = f'{self} + {other} = {Dirt()}'
            return new_obj
        else:
            return None
class Storm():
    def __str__(self):
        return 'Шторм'

class Steam():
    def __str__(self):
        return 'Пар'

class Dirt():
    def __str__(self):
        return 'Грязь'

class Lighting():
    def __str__(self):
        return 'Молния'

class Dust():
    def __str__(self):
        return 'Порох'

class Lava():
    def __str__(self):
        return 'Лава'
    def __add__(self, other):
        if str(other) == 'Вода':
            new_obj = f'{self} + {other} = {CobbleStone()}'
            return new_obj
        else:
            return None
class Obsidian():
    def __str__(self):
        return 'Обсідіан'
class CobbleStone():
    def __str__(self):
        return 'Камінь'

print(Water() + Air())
print(Water() + Fire())
print(Water() + Earth())
print(Air() + Earth())
print(Air() + Fire())
print(Fire() + Earth())
print(Lava() + Water())
print(Water() + Lava())
print(Water() + CobbleStone())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
