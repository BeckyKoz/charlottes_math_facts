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
        print("*****",self.num1)
        self.num2 = num2
        print("$$$$$",self.num2)

        self.operation = operation
        print("^^^^^",self.operation)

        self.correct_answer = self.OPERATIONS[operation](num1, num2)

    def ask(self):
        """Returns the question as a string"""
        return f"What is {self.num1} {self.operation} {self.num2}?"

    def check_answer(self, user_answer):
        """Checks if the user's answer is correct"""
        return int(user_answer) == self.correct_answer

class Quiz:
    def __init__(self):
        self.num_questions = 0
        self.question = self.generate_question()
        self.score = 0
        self.player = ""

    def generate_question(self):
        """Generates a random multiplication question"""
        operations = ["*"]
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operation = random.choice(operations)
        return Question(num1, num2, operation)

    def ask_question(self):
        """Generates question, asks it to user
        Returns user input"""

        # if self.player.needs_practice:
        #     self.question = self.get_needs_practice_question(self.player.needs_practice)
        # else:
        self.question = self.generate_question()
        user_answer = input(self.question.ask() + " ")
        self.num_questions += 1
        return user_answer

    def get_boolean_answer(self, user_answer):
        """Returns true if player answers correctly and returns false if not"""
        
        if self.question.check_answer(user_answer):
            return True
        else:
            return False

    def handle_result(self, result, player):
        """
        Handles appropriate workflow for correct/incorrect answer
        """
        if result:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The right answer is {self.question.correct_answer}\n")
            self.save_question(self.question, player.needs_practice)

    def get_score(self):
        """Returns the final score"""
        return f"You scored {self.score}/{self.num_questions}."
    
    def save_question(self, question, bank):
        """Saves wrongly answered questions to a bank of repeats"""
        bank.append(
            {
                "num1": question.num1, 
                "num2": question.num2, 
                "op": question.operation, 
                "ans": question.correct_answer
            })

    def get_needs_practice_question(self, bank):
        """Chooses a random question from the bank of needs_practice questions"""
        random_question = random.choice(bank)
        print(random_question)
        num1 = random_question.get("num1")
        num2 = random_question.get("num2")
        operation = random_question.get("op") 
        return Question(num1, num2, operation)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.needs_practice = []

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score
    

class QuizApp:
    def __init__(self):
        self.player = None
        self.quiz = Quiz()

    def start(self):
        """Starts the quiz"""
        print("Welcome to Charlotte's Math Facts!")
        self.player = Player("Charlotte")
        self.quiz.player = self.player
        self.run()

    def print_practice_questions(self, question_bank):
        print(f"Questions that still need practice:")  
        for q in question_bank:
            print("    ", q)

    def run(self):
        while True:
            user_answer = self.quiz.ask_question()
            result = self.quiz.get_boolean_answer(user_answer)
            self.quiz.handle_result(result, self.player)
            play_again = input("Press 'ENTER' to play again; 'Q' to quit").strip().lower()
            if play_again != "":
                print(f"Goodbye, {self.player.name}! {self.quiz.get_score()}")
                self.print_practice_questions(self.player.needs_practice)
                break

# Run the application
if __name__ == "__main__":
    app = QuizApp()
    app.start()
