from random import randint
from termcolor import cprint, colored


guess_number = None
gameover = None


def guess_numbers():
    global guess_number

    guess_number = randint(1000, 9999)
    return guess_number


def start_game():
    while True:
        number_user = input(colored('Введіть 4-х значен число: ', color='green'))
        if len(number_user) != 4:
            cprint('Введене число не є 4-значним!', color='red')
            continue
        else:
            break
    return number_user


def verify_number(number):

    global gameover

    verify_guess = []
    verify_put_number = []
    for numbers in ''.join(str(number)):
        verify_put_number.append(int(numbers))

    for numbers in ''.join(str(guess_number)):
        verify_guess.append(int(numbers))

    result = {'bulls': 0, 'cows': 0}
    for i, y in enumerate(verify_guess):

        if y == verify_put_number[i]:
            result['bulls'] += 1
        elif y in verify_put_number:
            result['cows'] += 1
    gameover = result['bulls']
    return result


def _is_gameover():
    return gameover == 4

