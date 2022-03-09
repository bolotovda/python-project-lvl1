from brain_games.logic import greet, tell_rules, do_qna, congrats, compare
from random import randint


def count_greatest(a, b):
    c = 0
    if a >= b:
        while a % b != 0:
            c = a % b
            a = b
            b = c
        return b
    else:
        while b % a != 0:
            c = b % a
            b = a
            a = c
        return a


def divide():
    greet()

    rule = 'Find the greatest common divisor of given numbers.'
    tell_rules(rule)

    i = 0
    while i < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)

        question = f'{num1} {num2}'

        correct_answer = count_greatest(num1, num2)

        answer = int(do_qna(question))

        result = compare(answer, correct_answer)
        if result is False:
            return

        i += 1

    congrats()
