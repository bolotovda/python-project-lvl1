import prompt


def lets_play(rule, ask_and_check):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rule)

    counter = 0
    amount_of_questions = 3
    while counter < amount_of_questions:
        question_and_correct_answer = ask_and_check()
        question = question_and_correct_answer[0]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        correct_answer = question_and_correct_answer[1]

        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
