# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


with open('registrations.txt', 'r', encoding='utf8') as text:
    for i in text:
        text_split = i.split(' ')
        try:
            if len(text_split) != 3:
                raise ValueError('НЕ присутсвуют все три поля')
            elif text_split[0].isalpha() is not True:
                raise NotNameError('поле имени содержит НЕ только буквы')
            elif '@' not in list(text_split[1]):
                raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')
            elif 10 < int(text_split[2]) > 99:
                raise ValueError('поле возраст НЕ является числом от 10 до 99')
            with open('registrations_good.log', 'a', encoding='utf8') as text:
                for j in text_split:
                    text.write(f'{j} ')

        except Exception as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as text:
                for j in text_split:
                    text.write(f'{j} ')
                text.write(f'Error - {exc.args}\n')
            continue
