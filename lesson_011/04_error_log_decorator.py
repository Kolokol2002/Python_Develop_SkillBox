# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

def log_errors(param):
    def log_errors2(func):
        def logger(*args, **kwargs):
            with open(param, 'a', encoding='utf8') as file:
                try:
                    func(*args, **kwargs)
                except Exception as exc:
                    file.write(f"Ім'я функції - {func.__name__}, "
                              f"Параметри функції - {str(*args)}, "
                              f"Тип помилки - {exc.__class__},"
                              f"Текс помилки - {exc}.\n")
        return logger

    return log_errors2


# Проверить работу на следующих функциях
@log_errors(param='function_errors.log')
def perky(param):
    return param / 0


@log_errors(param='function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')



for line in lines:
    check_line(line)

perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

