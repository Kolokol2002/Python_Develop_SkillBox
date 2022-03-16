# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def param(start_point, angle, length, vector, steps, step=0):
    if step > steps:
        return
    if step == 0:
        length += 1
    elif 0 <= step <= 1:
        length -= 1
    tri1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    tri1.draw()

    next_point = tri1.end_point
    step += 1
    next_angle = angle + vector

    param(start_point=next_point, angle=next_angle, vector=vector, steps=steps, length=length, step=step)


def get_polygon(n=3):
    if n == 3:
        def triangle(start_point, angle, length):
            param(start_point=start_point, angle=angle, length=length, vector=120, steps=2)
    elif n == 4:
        def triangle(start_point, angle, length):
            param(start_point=start_point, angle=angle, length=length, vector=90, steps=3)

    elif n == 5:
        def triangle(start_point, angle, length):
            param(start_point=start_point, angle=angle, length=length, vector=72, steps=4)

    elif n == 6:
        def triangle(start_point, angle, length):
            param(start_point=start_point, angle=angle, length=length, vector=60, steps=5)
    else:
        raise Exception('Сума сторін має бути в діапазоні 3-6!')

    return triangle

draw_triangle = get_polygon(n=3)
draw_triangle(start_point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
