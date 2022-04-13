# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import os
import time
from collections import defaultdict
from threading import Thread, Lock

start_time = time.time()

class Valatition(Thread):

    def __init__(self, file, lock, defaultlist):
        super().__init__()
        self.file = file
        self.all_info = defaultlist
        self.price = []
        self.name_ticket = None
        self.lock = lock

    def run(self):
        one_str = True
        with open(self.file, 'r', encoding='utf8') as info:
            for res in info:
                if one_str:
                    one_str = False
                    continue
                res = res.split(',')
                self.price.append(float(res[2]))
                if self.name_ticket == None:
                    self.name_ticket = res[0]
        average_price = (max(self.price) + min(self.price)) / 2
        volatility = ((max(self.price) - min(self.price)) / average_price) * 100
        with self.lock:
              self.all_info[self.name_ticket] += volatility
        self.price = []


start_dir = 'trades'
list_dir = os.listdir(start_dir)
all_info = defaultdict(int)
lock = Lock()

validation = [Valatition(file=f'{start_dir}/{dir}', lock=lock, defaultlist=all_info) for dir in list_dir]

for val in validation:
    val.start()

for val in validation:
    val.join()

null_validation = []
for tiket, value in list(all_info.items()):
    if value == 0.0:
        null_validation.append(tiket)
        all_info.pop(tiket)

null_validation.sort(key=lambda i: i[0])

list_key = list(all_info.items())
list_key.sort(key=lambda i: i[1])
print('Максимальная волатильность:')
print(''.join(reversed([f'{tiket} - {value} %\n' for tiket, value in list_key[-3:]])))

print('Минимальная волатильность:')
print(''.join(reversed([f'{tiket} - {value} %\n' for tiket, value in list_key[:3]])))

print('Нулевая волатильность:')
print(', '.join([tiket for tiket in null_validation]))

end_time = time.time()

res_time = round(end_time - start_time, 1)

print(res_time)