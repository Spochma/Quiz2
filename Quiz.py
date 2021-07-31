from classe import Question

question_prompts = [
    "What color is Banana!? \n a) Red \n b) Yellow \n c) Green \n\n",
    "What color is Strawberry!?\n a) Red \n b) Grey \n c) Blue \n\n",
    "What color is Apple!?\n a) Red/Green \n b) Pink \n c) black \n\n",
]

questions = [
    Question(question_prompts[0], 'b'),
    Question(question_prompts[1], 'a'),
    Question(question_prompts[2], 'a'),
]


def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))


run_quiz(questions)



