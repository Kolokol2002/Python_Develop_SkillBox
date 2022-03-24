# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def parser(file):
    res_list = {}
    with open(file, 'r', encoding='utf8') as text:
        for i in text:
            d = i.translate(str.maketrans('', '', '[]\n', ))
            date, time, text = d.split(' ')
            if 'NOK' == text:
                time = time.split(':')[:-1]
                time_res = f'{time[0]}:{time[1]}'
                if f'{date} {time_res}' not in res_list:
                    res_list[f'{date} {time_res}'] = 1
                else:
                    res_list[f'{date} {time_res}'] += 1

    for datatime, count in res_list.items():
        yield f'{datatime}: {count}'


grouped_events = parser('events.txt')
for group_time in grouped_events:
    print(group_time)
    # print(f'[{group_time}] {event_count}')