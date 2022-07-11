# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw, ImageColor

import argparse


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


def make_ticket(fio, from_, to, date, save_to):
    # TODO здесь ваш код
    im = Image.open('./images/ticket_template.png')

    font = ImageFont.truetype('Roboto-Black.ttf', size=15)

    draw_text = ImageDraw.Draw(im)
    draw_text.text((45, 122), fio, font=font, fill=ImageColor.colormap['black'])
    draw_text.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])
    draw_text.text((45, 260), to, font=font, fill=ImageColor.colormap['black'])
    draw_text.text((285, 260), date, font=font, fill=ImageColor.colormap['black'])
    if save_to == None:
        im.save('ticket_airplane.png')
    else:
        im.save(save_to)



# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('--fio', dest='fio', type=str)
parser.add_argument('--from', dest='from_', type=str)
parser.add_argument('--to', dest='to', type=str)
parser.add_argument('--date', dest='date', type=str)
parser.add_argument('--save_to', dest='save_to', type=str)

args = parser.parse_args()

make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save_to=args.save_to)
