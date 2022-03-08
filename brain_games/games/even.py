from brain_games.logic import greet, tell_rules, do_qna, congrats, compare
from random import randint


def is_even():
    greet()

    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    tell_rules(rule)

    i = 0
    while i < 3:
        question = randint(1, 100)

        answer = do_qna(question)

        if question % 2 == 0:
            correct_answer = 'yes'
        elif question % 2 != 0:
            correct_answer = 'no'

        result = compare(answer, correct_answer)
        if result is False:
            return

        i += 1

    congrats()
