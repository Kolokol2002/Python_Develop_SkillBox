# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

def draw_smile(x, y, color, whide, size):
    point = sd.get_point(x, y)
    sd.circle(point, (size * 12.5), color, whide)

    for i in range(1, 3):
        res_1 = x + (size * 6.25) if i % 2 == 0 else x - (size * 6.25)
        res_2 = x + (size * 3.75) if i % 2 == 0 else x - (size * 3.75)
        start = sd.get_point(res_1, y + (size * 6.25))
        end = sd.get_point(res_2, y + (size * 3.75))
        sd.line(start, end, color, whide)

        start_2 = sd.get_point(res_2, y + (size * 6.25))
        end_2 = sd.get_point(res_1, y + (size * 3.75))
        sd.line(start_2, end_2, color, whide)

    month_x = sd.get_point(x + (size * 1.25), y - (size * 5))
    month_y = sd.get_point(x - (size * 1.25), y - (size * 5))
    sd.line(month_x, month_y, color, whide)

    #body
    sd.line(sd.get_point(x, y - (size * 12.5)), sd.get_point(x, y - (size * 47.5)), color, whide)

    #hand
    sd.line(sd.get_point(x, y - (size * 17.5)), sd.get_point(x - (size * 15), y - (size * 22.5)), color, whide)
    sd.line(sd.get_point(x, y - (size * 17.5)), sd.get_point(x + (size * 15), y - (size * 22.5)), color, whide)

    #foot
    sd.line(sd.get_point(x, y - (size * 47.5)), sd.get_point(x - (size * 12.5), y - (size * 75)), color, whide)
    sd.line(sd.get_point(x, y - (size * 47.5)), sd.get_point(x + (size * 12.5), y - (size * 75)), color, whide)


# def draw_smile(x, y, color, whide, size=2):
#     point = sd.get_point(x, y)
#     sd.circle(point, size * 25, color, whide)
#
#     for i in range(1, 3):
#         res_1 = x + size25 if i % 2 == 0 else x - 25
#         res_2 = x + 15 if i % 2 == 0 else x - 15
#         start = sd.get_point(res_1, y + 25)
#         end = sd.get_point(res_2, y + 15)
#         sd.line(start, end, color, whide)
#
#         start_2 = sd.get_point(res_2, y + 25)
#         end_2 = sd.get_point(res_1, y + 15)
#         sd.line(start_2, end_2, color, whide)
#
#     month_x = sd.get_point(x + 5, y - 20)
#     month_y = sd.get_point(x - 5, y - 20)
#     sd.line(month_x, month_y, color, whide)
#
#     #body
#     sd.line(sd.get_point(x, y - 50), sd.get_point(x, y - 190), color, whide)
#
#     #hand
#     sd.line(sd.get_point(x, y - 70), sd.get_point(x - 60, y - 90), color, whide)
#     sd.line(sd.get_point(x, y - 70), sd.get_point(x + 60, y - 90), color, whide)
#
#     #foot
#     sd.line(sd.get_point(x, y - 190), sd.get_point(x - 50, y - 280), color, whide)
#     sd.line(sd.get_point(x, y - 190), sd.get_point(x + 50, y - 280), color, whide)
