from brain_games.logic import *
from random import randint, choice

def count():
    greet()
    
    rule = 'What is the result of the expression?'
    tell_rules(rule)

    ops = ['+', '-', '*']

    i = 0
    while i < 3:
        num1 = randint(0, 10)
        num2 = randint(1, 10)
        
        op = choice(ops)
        question = f'{num1} {op} {num2}'
        correct_answer = eval(str(num1) + op + str(num2))

        answer = int(do_qna(question))

        result = compare(answer, correct_answer)
        if result == False:
            return

        i += 1

    congrats()
