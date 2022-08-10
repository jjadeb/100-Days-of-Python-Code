import data
import random
import question_model


class QuizBrain:
    def __init__(self, q_list):
        self.questions_list = q_list
        self.question_num = 1
        self.score = 0
        self.total_questions = len(self.questions_list)
        self.questions_done = []
        self.keep_going = True

    def next_question(self):
        current_question = random.choice(self.questions_list)
        if current_question in self.questions_done:
            self.next_question()
        self.questions_done.append(current_question)
        question = current_question.text
        answer = current_question.answer
        user_answer = input(f"Question {self.question_num}: {question} (True/False): ").lower()
        self.check_answer(answer, user_answer)

    def still_has_questions(self):
        if self.question_num >= self.total_questions:
            print("Woohoo!! You win! There are no more questions.")
            self.keep_going = False
        return self.keep_going

    def check_answer(self, answer, user_answer):
        if answer == user_answer:
            self.score += 1
            print(f"That is correct! Your score is {self.score}.")
            self.question_num += 1
        else:
            print(f"That is incorrect. Your final score is {self.score}.")
            self.keep_going = False

