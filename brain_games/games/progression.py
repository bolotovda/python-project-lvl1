from random import randint
from brain_games import logic


RULE = 'What number is missing in the progression?'


def ask_and_check():
    progression = []
    first_number = randint(1, 50)
    step = randint(2, 5)
    amount_of_numbers = randint(5, 10)

    for n in range(0, amount_of_numbers):
        progression.append(first_number)
        first_number += step

    index_of_the_number = randint(0, len(progression) - 1)
    number = progression[index_of_the_number]

    progression.remove(number)
    progression.insert(index_of_the_number, '..')
    question = ' '.join(
        str(index_of_the_number) for index_of_the_number in progression)

    correct_answer = str(number)

    return question, correct_answer


def guess():
    logic.lets_play(RULE, ask_and_check)
