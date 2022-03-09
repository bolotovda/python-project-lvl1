import prompt


def greet():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def tell_rules(rule):
    print(rule)


def do_qna(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def compare(answer, correct_answer):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {name}!')
        return False


def congrats():
    print(f'Congratulations, {name}!')
