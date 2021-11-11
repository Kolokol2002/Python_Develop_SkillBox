# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные



# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код




N = 20

snowlist = []
for _ in range(N):
    snowlist.append([sd.random_number(50, 700), sd.random_number(550, 1200), sd.random_number(10, 25)])

while True:

    for i, (x, y, length) in enumerate(snowlist):
        point = sd.get_point(x, y)
        sd.start_drawing()
        sd.snowflake(center=point, length=length, color=sd.background_color)
        random_x = sd.random_number(-10, 10)
        last_point = sd.get_point(x + random_x, y - 10)
        snowlist[i][1] -= 10
        snowlist[i][0] += random_x
        sd.snowflake(center=last_point, length=length, color=sd.COLOR_WHITE)

        if y < length*2:
            # sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
            snowlist[i][1] += sd.random_number(400, 700)
            continue

        sd.finish_drawing()
        sd.sleep(0.01)
    if sd.user_want_exit():
        break

sd.pause()
# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


