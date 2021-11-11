# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

sd.set_screen_size(1000, 1000)


def param(start_point, angle, length, vector, steps, color, step=0):
    if step > steps:
        return
    if step == 0:
        length += 1
    elif 0 <= step <= 1:
        length -= 1
    res = sd.get_vector(start_point=start_point, angle=angle, length=length)
    res.draw(color=color)

    next_point = res.end_point
    next_angle = angle + vector
    step += 1
    param(start_point=next_point, angle=next_angle, vector=vector, steps=steps, length=length, color=color, step=step)



def tri(start_point, angle=0, length=100, color=sd.COLOR_RED):
    param(start_point=start_point, angle=angle, length=length, vector=120, steps=2, color=color)


def four(start_point, angle=0, length=100, color=sd.COLOR_RED):
    param(start_point=start_point, angle=angle, length=length, vector=90, steps=3, color=color)


def five(start_point, angle=0, length=100, color=sd.COLOR_RED):
    param(start_point=start_point, angle=angle, length=length, vector=72, steps=4, color=color)


def six(start_point, angle=0, length=100, color=sd.COLOR_RED):
    param(start_point=start_point, angle=angle, length=length, vector=60, steps=5, color=color)


print(
    'Цвета:\n'
    '  0 : red\n'
    '  1 : orange\n'
    '  2 : yellow\n'
    '  3 : green\n'
    '  4 : cyan\n'
    '  5 : blue\n'
    '  6 : purple\n'
)
value = int(input('Введіть бажаний колір: '))
while value > 6:
    print('Номер не вірний')
    value = int(input('Введіть бажаний колір: '))

colors = {
    0: sd.COLOR_RED,
    1: sd.COLOR_ORANGE,
    2: sd.COLOR_YELLOW,
    3: sd.COLOR_GREEN,
    4: sd.COLOR_CYAN,
    5: sd.COLOR_BLUE,
    6: sd.COLOR_PURPLE
}

color_res = colors[value]

start_point = sd.get_point(200, 300)
tri(start_point=start_point, angle=90, length=200, color=color_res)

start_point = sd.get_point(300, 100)
four(start_point=start_point, angle=20, length=100, color=color_res)

start_point = sd.get_point(300, 600)
five(start_point=start_point, angle=60, length=100, color=color_res)

start_point = sd.get_point(600, 300)
six(start_point=start_point, angle=70, length=100, color=color_res)

sd.pause()
