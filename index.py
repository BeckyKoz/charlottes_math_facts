# Charlotte's Math Facts

import random 
import operator

class Question:
    '''
    Math fact question

    Receives as input: two integers, one operator

    '''

    OPERATIONS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv
    }
    
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        self.correct_answer = self.OPERATIONS[operation](num1, num2)

    def ask(self):
        """Returns the question as a string"""
        return f"What is {self.num1} {self.operation} {self.num2}?"

    def check_answer(self, user_answer):
        """Checks if the user's answer is correct"""
        return int(user_answer) == self.correct_answer

class Quiz:
    def __init__(self, num_questions=5):
        self.num_questions = num_questions
        self.questions = self.generate_questions()
        self.score = 0

    def generate_questions(self):
        """Creates a list of random math questions"""
        questions = []
        # operations = ["+", "-", "*", "/"]
        operations = ["*"]
        for _ in range(self.num_questions):
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            operation = random.choice(operations)
            # Avoid division by zero or fractions
            if operation == "/" and num2 == 0:
                num2 = 1
            question = Question(num1, num2, operation)
            questions.append(question)
        return questions

    def ask_questions(self):
        """Loops through questions and gets user input"""
        for question in self.questions:
            user_answer = input(question.ask() + " ")
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The right answer is {question.correct_answer}\n")

    def get_score(self):
        """Returns the final score"""
        return f"You scored {self.score}/{self.num_questions}."


class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def save_score(self, score):
        """Saves the latest quiz score"""
        self.scores.append(score)

    def get_scores(self):
        """Returns the history of scores"""
        return self.scores

class QuizApp:
    def __init__(self):
        self.player = None

    def start(self):
        """Starts the quiz application"""
        print("Welcome to Charlotte's Math Facts!")
        # name = input("Enter your name: ")
        self.player = Player("Charlotte")

        while True:
            quiz = Quiz()
            quiz.ask_questions()
            score = quiz.get_score()
            print(score)

            self.player.save_score(score)

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print(f"Goodbye, {self.player.name}! Your scores: {self.player.get_scores()}")
                break

# Run the application
if __name__ == "__main__":
    app = QuizApp()
    app.start()
