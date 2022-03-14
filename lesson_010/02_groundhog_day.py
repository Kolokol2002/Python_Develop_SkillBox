# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


carma_count = 0

list_excepts = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError,
                SuicideError]

def one_day():
    global carma_count
    carma = random.randint(1, 7)
    carma_count += carma
    excepts = random.randint(1, 13)
    if excepts == 1:
        random_excepts = random.choice(list_excepts)

        raise random_excepts(random_excepts)

while carma_count <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        one_day()
    except Exception as exc :
        print(f'Оппа, ошибочка - {exc}')

# https://goo.gl/JnsDqu
