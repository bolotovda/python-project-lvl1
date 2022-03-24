from random import randint, choice
from brain_games import logic
from operator import add, sub, mul


RULE = 'What is the result of the expression?'


def prepare_data():
    operators = {'+': add, '-': sub, '*': mul}
    first_operand = randint(0, 10)
    second_operand = randint(1, 10)

    operator = choice(list(operators))
    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(operators[operator](first_operand, second_operand))

    return question, correct_answer


def input_rule_and_data():
    logic.run_game(RULE, prepare_data)
