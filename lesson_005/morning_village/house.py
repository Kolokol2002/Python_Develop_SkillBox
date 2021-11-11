# -*- coding: utf-8 -*-

# (цикл for)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
import simple_draw as sd


def draw_house(width_brick, height_brick, color, width):

    for row in range(2, 21):
        OFFSET = height_brick if row % 2 == 0 else 0
        for brick in range(9, 18):
            left_bottom_x = OFFSET + width_brick * brick
            left_bottom_y = height_brick * row
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)

            right_top_x = left_bottom_x + width_brick
            right_top_y = left_bottom_y + height_brick
            right_top = sd.get_point(right_top_x, right_top_y)

            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=color, width=width)

    sd.square(left_bottom=sd.get_point(450, 50), side=475, color=color, width=width)

    points = [sd.get_point(400, 525), sd.get_point(975, 525), sd.get_point(680, 700)]
    sd.polygon(point_list=points, color=sd.COLOR_DARK_RED, width=0)


