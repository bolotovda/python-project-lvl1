from random import randint
import prompt


def choice():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        a = prompt.string('Your ans: ')
        if question % 2 == 0:
            c = 'yes'
        elif question % 2 != 0:
            c = 'no'
        if a == c:
            print('Correct!')
            i += 1
        else:
            print(f'\'{a}\' is wrong answer ;(. Correct answer was \'{c}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
