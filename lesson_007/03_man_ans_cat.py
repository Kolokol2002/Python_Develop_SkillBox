# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 20:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 20
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_for_cat(self):
        if self.house.money >= 50:
            cprint('{} купил еду для кота'.format(self.name), color='magenta')
            self.house.food_cat += 50
            self.house.money -= 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning(self):
        cprint('{} убрал за котом'.format(self.name), color='green')
        self.house.dirt -= 100
        self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return

        dice = randint(1, 3)
        if self.house.money <= 50:
            self.work()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.food_cat <= 20:
            self.shopping_for_cat()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.dirt >= 100:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:

    def __init__(self, name):
        self.name = f'Кот {name}'
        self.house = None
        self.fullness_cat = 50

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness_cat)

    def eat(self):
        if self.house.food_cat >= 10:
            cprint('{} кушал'.format(self.name), color='yellow')
            self.fullness_cat += 20
            self.house.food_cat -= 10
        else:
            cprint('{} нет еды для кота'.format(self.name), color='red')

    def sleep(self):
        cprint('{} Поспал'.format(self.name), color='blue')
        self.fullness_cat -= 10

    def tear_wallpaper(self):
        cprint('{} драл обои'.format(self.name), color='green')
        self.fullness_cat -= 10
        self.house.dirt += 5

    def go_to_the_house(self, house):
        self.house = house
        cprint("{}`а подобрали в дом".format(self.name), color="cyan")

    def act(self):
        if self.fullness_cat < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness_cat <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        else:
            self.tear_wallpaper()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_cat = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кошки осталось {},' \
               ' грязи в доме {}'.format(self.food, self.money, self.food_cat, self.dirt)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни')
]
cats = [
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),
    Cat(name='Мурчик'),

]

my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
for cat in cats:
    cat.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.act()

    print('--- в конце дня ---')

    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)

    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
