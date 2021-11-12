# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

import snowfall as sf

sf.create_snowfall(16)
while True:
    sd.start_drawing()
    sf.draw_snowfall_color(color=sd.background_color)
    sf.move_snowfall()
    sf.draw_snowfall_color(color=sd.COLOR_WHITE)
    if sf.number_snowfall_down_screen():
        sf.del_snowfall()
        sf.create_snowfall(1)
    sd.finish_drawing()
    sd.sleep(0.15)
    if sd.user_want_exit():
        break

sd.pause()
