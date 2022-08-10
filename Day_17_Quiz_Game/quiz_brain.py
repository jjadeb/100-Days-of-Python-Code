
import random


class QuizBrain:
    """Represents the quiz"""
    def __init__(self, q_list):
        self.questions_list = q_list
        self.question_num = 1
        self.score = 0
        self.total_questions = len(self.questions_list)
        self.questions_left = q_list
        self.keep_going = True

    def next_question(self):
        """Provides a new quesiton and takes the user's answer"""
        current_question = random.choice(self.questions_left)
        self.questions_left.remove(current_question)
        question = current_question.text
        answer = current_question.answer
        user_answer = input(f"Question {self.question_num}: {question} (True/False): ").lower()
        self.check_answer(answer, user_answer)

    def still_has_questions(self):
        """Checks to see if anymore questions should be provided"""
        if self.question_num > self.total_questions:
            print("Woohoo!! You win! There are no more questions.")
            self.keep_going = False
        return self.keep_going

    def check_answer(self, answer, user_answer):
        """Checks to see if the user's answer is correct"""
        if answer == user_answer:
            self.score += 1
            print(f"That is correct! Your score is {self.score}.")
            self.question_num += 1
        else:
            print(f"That is incorrect. Your final score is {self.score}.")
            self.keep_going = False

