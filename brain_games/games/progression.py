from brain_games.logic import greet, tell_rules, do_qna, congrats, compare
from random import randint


def get_list():
    i = 0
    progression = [randint(1, 50)]
    add = randint(2, 5)
    while i < randint(4, 9):
        progression += [progression[i] + add]
        i += 1

    x = randint(0, len(progression) - 1)

    global number
    number = progression[x]

    progression.remove(number)
    progression.insert(x, '..')

    return progression


def progress():
    greet()

    rule = 'What number is missing in the progression?'
    tell_rules(rule)

    i = 0
    while i < 3:
        question = ' '.join(str(x) for x in get_list())

        correct_answer = number

        answer = int(do_qna(question))

        result = compare(answer, correct_answer)
        if result is False:
            return

        i += 1

    congrats()
