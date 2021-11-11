# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


all_folks = []
from district.central_street.house1 import room1, room2
all_folks.extend(room1.folks)
all_folks.extend(room2.folks)


from district.central_street.house2 import room1, room2
all_folks.extend(room1.folks)
all_folks.extend(room2.folks)

print("На Цетральній вулиці живе: ", ", ".join(all_folks))

all_folks_soviet = []
from district.soviet_street.house2 import room1, room2
all_folks_soviet.extend(room1.folks)
all_folks_soviet.extend(room2.folks)

from district.soviet_street.house2 import room1, room2

all_folks_soviet.extend(room1.folks)
all_folks_soviet.extend(room2.folks)

print("На Вулиці Совет живе: ", ", ".join(all_folks_soviet))

