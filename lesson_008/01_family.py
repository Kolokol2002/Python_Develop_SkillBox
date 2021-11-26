# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    count_money = 0
    count_food = 0
    count_coat = 0
    count = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        self.count += 1
        if self.count == 365:
            return f'В доме: денег - {self.money}, еды - {self.food}, грязи - {self.dirt}\n\n'\
                   f'За год: заработано денег - {self.count_money}, ' \
                   f'сьедено еды - {self.count_food}, куплено шуб - {self.count_coat}'
        else:
            return f'В доме: денег - {self.money}, еды - {self.food}, грязи - {self.dirt}'


class Family:

    def __init__(self, name):
        self.name = f'{self.__class__.__name__} {name}'
        self.fullness = 30
        self.happy = 100
        self.house = None

    def __str__(self):
        return f'У {self.__class__.__name__}, сытость - {self.fullness}, счастья - {self.happy}'

    def in_house(self, house):
        self.house = house


class Husband(Family):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def in_house(self, house):
        super().in_house(house=house)

    def act(self):
        self.house.dirt += 5

        count = randint(1, 2)

        if self.happy < 10:
            cprint(f'{self.name} - умер от депресии(', color='red')
            return
        if self.fullness < 0:
            cprint(f'{self.name} - умер от недостатка еды((', color='red')
            return

        if self.house.dirt > 90:
            cprint(f'У {self.name} - счастья упало на 10, много грязи', color='red')
            self.happy -= 10
        elif self.fullness <= 20:
            self.eat()
        elif self.house.money <= 20:
            self.work()
        elif self.happy <= 20:
            self.gaming()
        elif count == 1:
            self.gaming()
        elif count == 2:
            self.work()

    def eat(self):
        count = randint(1, 30)
        self.fullness += count
        self.house.food -= count
        self.house.count_food += count
        cprint(f'{self.name} - поел {count} едениц еды', color='green')

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        self.house.count_money += 150
        cprint(f'{self.name} - работал', color='magenta')

    def gaming(self):
        self.happy += 20
        self.fullness -= 10
        cprint(f'{self.name} - играл WoT', color='yellow')


class Wife(Family):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def in_house(self, house):
        super().in_house(house=house)

    def act(self):

        count = randint(1, 2)

        if self.happy < 10:
            cprint(f'{self.name} - умерла от депресии(', color='red')
            return
        if self.fullness < 0:
            cprint(f'{self.name} - умерла от недостатка еды((', color='red')
            return

        if self.house.dirt >= 90:
            cprint(f'У {self.name} - счастья упало на 10, много грязи', color='red')
            self.happy -= 10
            self.clean_house()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.food <= 60:
            self.shopping()
        elif self.happy <= 20:
            self.buy_fur_coat()
        elif count == 1:
            self.eat()
        elif count == 2:
            cprint(f'{self.name} ничего не делала', color='yellow')

    def eat(self):
        count = randint(1, 30)
        self.house.food -= count
        self.fullness += count
        self.house.count_food += count
        cprint(f'{self.name} - поела {count} едениц еды', color='green')

    def shopping(self):
        self.fullness -= 10
        self.house.food += 30
        self.house.money -= 30
        cprint(f'{self.name} - купила еду', color='blue')

    def buy_fur_coat(self):
        self.house.money -= 350
        self.happy += 60
        self.fullness -= 10
        self.house.count_coat = 1
        cprint(f'{self.name} - купила шубу и очень счаслива)', color='blue')

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt >= 90:
            self.house.dirt -= 90
        else:
            self.house.dirt -= self.house.dirt
        cprint(f'{self.name} - убралась в доме', color='red')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

members = [
    serge,
    masha,
]

for member in members:
    member.in_house(house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    for member in members:
        member.act()
    for member in members:
        cprint(member, color='cyan')

    cprint(home, color='cyan')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

