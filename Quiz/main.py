# Name:                   Amir Aslamov
# Description of Program: This program is designed to simulate the game of a quiz with
#                         true or false questions. The program also calculates and prints the
#                         score of the player.
# Date of Creation:       Sep 11, 2021, at 12:45 PM, Florida, U.S.



from question_model import Question
from data import question_data1
from quiz_brain import QuizBrain

question_bank = list()

for item in question_data1:
    q_text = item["question"]
    q_answer = item["correct_answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your total score is: {quiz.score}/{len(quiz.question_list)}")
