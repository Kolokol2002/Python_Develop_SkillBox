from random import randint


def bowling_count(round=10, balls=None):
    result = []
    for _ in range(round):
        random_number = 10
        for throw in range(2):
            if balls == None:
                balls = randint(0, random_number)
            if throw == 0:
                random_number -= balls
            if throw == 1:
                if balls == random_number:
                    result.append('/')
                    break
            if balls == 10:
                result.append('X')
                break
            elif balls == 0:
                result.append('-')
            else:
                result.append(str(balls))
            if balls != None and balls != 3:
                balls = 10 - balls
    return result


