from random import randint
from brain_games import logic


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    counter = 2
    while question % counter != 0:
        counter += 1
    return counter == question


def ask_and_check():
    question = randint(1, 100)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def verify_prime_number():
    logic.lets_play(RULE, ask_and_check)
