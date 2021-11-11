# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# sd.get_point()
# sd.get_vector()
# sd.line()
sd.set_screen_size(1000, 1000)

def param (start_point, angle, length, vector, steps, step=0,):
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


def tri (start_point, angle=0, length=100):
    param(start_point=start_point, angle=angle, length=length, vector=120, steps=2)

def four (start_point, angle=0, length=100):
    param(start_point=start_point, angle=angle, length=length, vector=90, steps=3)

def five (start_point, angle=0, length=100, step=0):
    param(start_point=start_point, angle=angle, length=length, vector=72, steps=4)

def six (start_point, angle=0, length=100, step=0):
    param(start_point=start_point, angle=angle, length=length, vector=60, steps=5)


start_point = sd.random_point()
tri(start_point=start_point, angle=90, length=200)

start_point = sd.random_point()
four(start_point=start_point, angle=20, length=100)

start_point = sd.random_point()
five(start_point=start_point, angle=60, length=100)

start_point = sd.random_point()
six(start_point=start_point, angle=70, length=100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
