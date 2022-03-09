from brain_games.logic import greet, tell_rules, do_qna, congrats, compare
from random import randint


def is_prime(x):
    i = 2
    while x % i != 0:
        i += 1
    if x == i:
        return True
    return False


def is_prime_main():
    greet()

    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    tell_rules(rule)

    i = 0
    while i < 3:
        question = randint(1, 100)

        answer = do_qna(question)

        if is_prime(question) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        result = compare(answer, correct_answer)
        if result is False:
            return

        i += 1

    congrats()
