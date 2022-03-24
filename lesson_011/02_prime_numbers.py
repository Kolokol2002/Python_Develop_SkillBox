# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import time


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# print(get_prime_numbers(10000))

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.n, self.i = n, 0

    def __iter__(self):
        self.i = 1
        self.prime_numbers = []
        return self

    def __next__(self):
        self.i += 1
        if self.i == self.n:
            raise StopIteration()
        for prime in self.prime_numbers:
            if self.i % prime == 0:
                return PrimeNumbers.__next__(self)
        else:
            self.prime_numbers.append(self.i)
        return self.i


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime = []
    for number in range(2, n + 1):
        for i in prime:
            if number % i == 0:
                break
        else:
            prime.append(number)
            yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


started_at = time.time()

def fibonacci_number():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 30:
            return

def future_number(list):
    if len(list) == 5:
        return int(list[0]) + int(list[1]) == int(list[3]) + int(list[4])
    else:
        return list[0] == list[-1]

def palindrom_number(list):
    list_reversed = list.copy()
    list_reversed.reverse()
    return list == list_reversed


def numbers_generator(n):
    prime = []
    for number in range(2, n + 1):
        for i in prime:
            if number % i == 0:
                break
        else:
            prime.append(number)
            list_int = list(str(number))
            for val in fibonacci_number():
                if val > number:
                    break
                elif str(number) in str(val):
                    yield number, fibonacci_number.__name__
                    break
            if len(list_int) == 1:
                continue
            if palindrom_number(list_int):
                yield number, palindrom_number.__name__
            if future_number(list_int):
                yield number, future_number.__name__


started_at = time.time()

for number in numbers_generator(n=10000):
    print(number)

ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Функция работала {elapsed} секунд(ы)')



