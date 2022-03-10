from random import randint
from brain_games import logic


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask():
    question = randint(1, 100)
    return question


def check_conditions(question):
    i = 2
    while question % i != 0:
        i += 1
    if question == i:
        return 'yes'
    return 'no'


def is_prime():
    logic.lets_play(rule, ask, check_conditions)
