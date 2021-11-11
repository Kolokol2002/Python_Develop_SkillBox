# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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
    'Виберіть фігуру:\n'
    '  0 : Трикутник\n'
    '  1 : Квадрат\n'
    "  2 : П'ятикутник\n"
    '  3 : Шестикутник\n'
)


value_figure = int(input('Введіть бажану фігуру: '))
while value_figure > 3:
    print('Номер не вірний')
    value_figure = int(input('Введіть бажану фігуру: '))


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

colors = {
    0: sd.COLOR_RED,
    1: sd.COLOR_ORANGE,
    2: sd.COLOR_YELLOW,
    3: sd.COLOR_GREEN,
    4: sd.COLOR_CYAN,
    5: sd.COLOR_BLUE,
    6: sd.COLOR_PURPLE
}

value_color = int(input('Введіть бажаний колір: '))
while value_color > 6:
    print('Номер не вірний')
    value = int(input('Введіть бажаний колір: '))

color_res = colors[value_color]

figures = {
    0: tri,
    1: four,
    2: five,
    3: six
}
figure = figures[value_figure]

start_point = sd.get_point(600, 500)
figure(start_point=start_point, angle=90, length=200, color=color_res)


sd.pause()

