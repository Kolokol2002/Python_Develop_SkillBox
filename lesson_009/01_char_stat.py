# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


file = 'Война и Мир, 1 том.txt'

class War_World():

    def __init__(self):
        self.count_words = {}
        self.init()


    def init(self,):
        with open(file, 'r', encoding='utf8') as text:
            for i in text:
                for y in i:
                    if y.isalpha():
                        if y in self.count_words:
                            self.count_words[y] += 1
                        else:
                            self.count_words[y] = 0

    def sort_alphabet_decrease(self):

        list_d = list(self.count_words.items())
        list_d.sort(key=lambda i: i[0])

        print(f'+---------+----------+\n|  буква  |  частота |\n+---------+----------+')
        for i in list_d:
            world = i[0].center(9, ' ')
            values = str(i[1]).center(10, ' ')
            print(f'|{world}|{values}|')

        total_count_worlds = 0
        for i in list_d:
            total_count_worlds += i[1]

        print(f'+---------+----------+\n|  итого  |{str(total_count_worlds).center(9, " ")} |'
              f'\n+---------+----------+')

    def sort_alphabet_increase(self):

        list_d = list(self.count_words.items())
        list_d.sort(key=lambda i: i[0])
        list_d.reverse()

        print(f'+---------+----------+\n|  буква  |  частота |\n+---------+----------+')
        for i in list_d:
            world = i[0].center(9, ' ')
            values = str(i[1]).center(10, ' ')
            print(f'|{world}|{values}|')

        total_count_worlds = 0
        for i in list_d:
            total_count_worlds += i[1]

        print(f'+---------+----------+\n|  итого  |{str(total_count_worlds).center(9, " ")} |'
              f'\n+---------+----------+')

    def sort_increase(self):

        sorted_dict = {}
        sorted_keys = sorted(self.count_words, key=self.count_words.get)

        for w in sorted_keys:
            sorted_dict[w] = self.count_words[w]

        print(f'+---------+----------+\n|  буква  |  частота |\n+---------+----------+')
        for key, values in sorted_dict.items():
            world = key.center(9, ' ')
            values = str(values).center(10, ' ')
            print(f'|{world}|{values}|')

        total_count_worlds = 0
        for i in sorted_dict.values():
            total_count_worlds += i

        print(f'+---------+----------+\n|  итого  |{str(total_count_worlds).center(9, " ")} |'
              f'\n+---------+----------+')







war_and_world = War_World()
# war_and_world.sort_alphabet_increase()
# war_and_world.sort_alphabet_decrease()
war_and_world.sort_increase()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
