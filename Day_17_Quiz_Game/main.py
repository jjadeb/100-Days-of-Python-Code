from data import question_data
from quiz_brain import QuizBrain
from question_model import Question
import os


question_bank = []
for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)


def play_quiz_game():
    """Starts the quiz and loops through questions."""
    print("Welcome to my Europe Quiz!")
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    yes_no = input("Would you like to play again? (y/n): ").lower()
    if yes_no == "y":
        os.system("clear")
        play_quiz_game()
    else:
        quit(0)


play_quiz_game()



