# -*- coding: utf-8 -*-



# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

import simple_draw as sd

def draw_tree(start_point, angle, length, width):
    color = sd.COLOR_DARK_YELLOW
    if length < 1:
        return
    if length < 4:
        color = sd.COLOR_GREEN
        width = 1
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v1.draw(color=color)
    random_angle = sd.random_number(30, 40)
    random_length = sd.random_number(60, 75)
    next_point = v1.end_point
    next_angle = angle + random_angle
    next_length = length * random_length/100
    draw_tree(start_point=next_point, angle=next_angle, length=next_length, width=width)
    draw_tree(start_point=v1.end_point, angle=angle-random_angle, length=next_length, width=width)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()



