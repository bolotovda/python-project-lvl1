from random import randint
from brain_games import logic


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_and_check():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def verify_evenness():
    logic.lets_play(RULE, ask_and_check)
