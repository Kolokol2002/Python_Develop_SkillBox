# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

from morning_village import smile, tree, rainbow, house, snowfall, sun
import simple_draw as sd

sd.resolution = (1600, 1000)
sd.background_color = sd.COLOR_DARK_BLUE



sd.rectangle(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(1600, 50), color=sd.COLOR_DARK_GREEN)

snowlist = []
for _ in range(20):
    snowlist.append([sd.random_number(50, 300), sd.random_number(300, 600), sd.random_number(4, 10)])

smile.draw_smile(x=1000, y=260, color=sd.COLOR_DARK_ORANGE, whide=2, size=3)
house.draw_house(width_brick=50, height_brick=25, color=sd.COLOR_DARK_YELLOW, width=2)
rainbow.draw_rainbow(x=-100, y=-500, radius=2000, width=10)
sun.draw_sun(x=160, y=830, size=3)
tree.draw_tree(start_point=sd.get_point(x=1300, y=45), angle=90, length=150, width=2)
snowfall.draw_snowfall(snowlist)


sd.pause()
