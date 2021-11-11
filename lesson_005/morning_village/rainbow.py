# -*- coding: utf-8 -*-

# (цикл for)



# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# start_x = 50
# end_x = 350
# for colors in rainbow_colors:
#     start_x += 5
#     end_x += 5
#     start_point = sd.get_point(start_x, 50)
#     end_point = sd.get_point(end_x, 450)
#     sd.line(start_point, end_point, colors, 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_rainbow(x, y, radius, width):

    for colors in rainbow_colors:
        radius -= width
        point = sd.get_point(x, y)
        sd.circle(center_position=point, radius=radius, color=colors, width=width)


