from random import randint
from brain_games import logic


rule = 'Find the greatest common divisor of given numbers.'


def ask():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    return question


def check_conditions(question):
    new_list = list(question.split(" "))
    a = int(new_list[0])
    b = int(new_list[1])
    c = 0

    if a >= b:
        while a % b != 0:
            c = a % b
            a = b
            b = c
        correct_answer = b
    else:
        while b % a != 0:
            c = b % a
            b = a
            a = c
        correct_answer = a
    return correct_answer


def chose():
    logic.lets_play(rule, ask, check_conditions)
