from random import randint
from brain_games import logic


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def prepare_data():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def input_rule_and_data():
    logic.run_game(RULE, prepare_data)
