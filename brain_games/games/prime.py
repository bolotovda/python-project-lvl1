from random import randint
from brain_games import logic


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question > 1:
        for i in range(2, question):
            if (question % i) == 0:
                return False
        else:
            return True
    else:
        return False


def prepare_data():
    question = randint(1, 100)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def input_rule_and_data():
    logic.run_game(RULE, prepare_data)
