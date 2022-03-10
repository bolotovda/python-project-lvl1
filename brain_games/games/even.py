from random import randint
from brain_games import logic


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask():
    question = randint(1, 100)
    return question


def check_conditions(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return correct_answer


def is_even():
    logic.lets_play(rule, ask, check_conditions)
