import prompt


def lets_play(rule, ask, check_conditions):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rule)

    i = 0
    while i < 3:
        question = ask()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        correct_answer = check_conditions(question)

        if str(answer) == str(correct_answer):
            print('Correct!')
            i += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
