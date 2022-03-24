from random import randint
from brain_games import logic


RULE = 'Find the greatest common divisor of given numbers.'


def define_gcd(first_number, second_number):
    buffer = 0
    gcd = 0
    if first_number >= second_number:
        while first_number % second_number != 0:
            buffer = first_number % second_number
            first_number = second_number
            second_number = buffer
        gcd = second_number
    else:
        while second_number % first_number != 0:
            buffer = second_number % first_number
            second_number = first_number
            first_number = buffer
        gcd = first_number
    return gcd


def prepare_data():
    first_number = randint(1, 100)
    second_number = randint(1, 100)

    question = f'{first_number} {second_number}'
    correct_answer = str(define_gcd(first_number, second_number))

    return question, correct_answer


def input_rule_and_data():
    logic.run_game(RULE, prepare_data)
