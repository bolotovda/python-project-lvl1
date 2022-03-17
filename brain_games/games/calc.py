from random import randint, choice
from brain_games import logic


RULE = 'What is the result of the expression?'


def ask_and_check():
    operands = ['+', '-', '*']
    first_operator = randint(0, 10)
    second_operator = randint(1, 10)

    operand = choice(operands)
    question = f'{first_operator} {operand} {second_operator}'
    correct_answer = str(eval(question))

    return question, correct_answer


def calculate():
    logic.lets_play(RULE, ask_and_check)
