# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1500, 900)

class Snowflake:
    snowlist = []

    def get_flakes(self, count):

        for _ in range(count):
            self.snowlist.append([sd.random_number(50, 700), sd.random_number(550, 1200), sd.random_number(10, 25)])

    def clear_previous_picture(self):
        sd.start_drawing()
        for x, y, length in self.snowlist:
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.background_color)

    def move(self):
        for i in range(len(self.snowlist)):
            random_x = sd.random_number(-10, 10)
            self.snowlist[i][1] -= 10
            self.snowlist[i][0] += random_x

    def draw(self):
        for x, y, length in self.snowlist:
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
        sd.finish_drawing()

    def can_fall(self):
        list_snow_down = []
        for i, (x, y, length) in enumerate(self.snowlist):
            if y < length * 2:
                list_snow_down.append(self.snowlist[i])
        for i in list_snow_down:
            self.snowlist.remove(i)

        return list_snow_down

    # TODO здесь ваш код


flake = Snowflake()
flake.get_flakes(count=10)

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if flake.can_fall():
        flake.get_flakes(count=1)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
