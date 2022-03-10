from random import randint, choice
from brain_games import logic


rule = 'What is the result of the expression?'


def ask():
    ops = ['+', '-', '*']
    num1 = randint(0, 10)
    num2 = randint(1, 10)
    op = choice(ops)
    question = f'{num1} {op} {num2}'
    return question


def check_conditions(question):
    correct_answer = eval(question)
    return correct_answer


def calculate():
    logic.lets_play(rule, ask, check_conditions)
