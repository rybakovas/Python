# from Question import question

from Python.basic.Question import Question

question_prompt = [
    "What color are Apples?\n(A) Red / Green\n(B) Purple\n(C) Orange\n\n",
    "What color are Bananas?\n(A) Teal\n(B) Magenta\n(C) Yellow\n\n",
    "What color are Strawberries?\n(A) Yellow\n(B) Red\n(C) Blue\n\n",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score += 1
    print("You got {} / {} correct".format(score, len(questions)))


run_test(questions)


# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor