# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class Parser:

    def __init__(self):
        self.remove_excess = []
        with open('events.txt', 'r', encoding='utf8') as text:
            for i in text:
                d = i.translate(str.maketrans('', '', '[]\n', ))
                y = d.split(' ')
                self.remove_excess.append(y)

    def pars(self):
        test_list = []
        for date, time, text in self.remove_excess:
            if 'NOK' == text:
                time_parse = [time.split(':')[:-1]]

                for hour, minute in time_parse:
                    test_list.append([date, f'{hour}:{minute}', text])

        res_list = {}

        for date, time, text in test_list:
            if f'{date} {time}' not in res_list:
                res_list[f'{date} {time}'] = 1
            else:
                res_list[f'{date} {time}'] += 1

        for datatime, count in res_list.items():
            print(f'{datatime}: {count}')


parser = Parser()
parser.pars()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
