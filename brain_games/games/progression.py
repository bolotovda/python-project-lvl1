from random import randint
from brain_games import logic


rule = 'What number is missing in the progression?'


def ask():
    i = 0
    progression = [randint(1, 50)]
    add = randint(2, 5)
    while i < randint(4, 9):
        progression += [progression[i] + add]
        i += 1

    x = randint(0, len(progression) - 1)

    global number
    number = progression[x]

    progression.remove(number)
    progression.insert(x, '..')
    question = ' '.join(str(x) for x in progression)
    return question


def check_conditions(question):
    correct_answer = number
    return correct_answer


def guess():
    logic.lets_play(rule, ask, check_conditions)
