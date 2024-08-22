import random

class QuizGame:
    def __init__(self):
        self.questions = {
            "General Knowledge": [
                {
                    "question": "What is the capital of France?",
                    "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                    "answer": "C"
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
                    "answer": "B"
                }
            ],
            "Literature": [
                {
                    "question": "Who wrote 'To Kill a Mockingbird'?",
                    "options": ["A) Mark Twain", "B) Harper Lee", "C) Jane Austen", "D) Charles Dickens"],
                    "answer": "B"
                }
            ]
        }
        self.score = 0

    def display_banner(self, text):
        print("\n" + "*" * (len(text) + 4))
        print(f"* {text} *")
        print("*" * (len(text) + 4) + "\n")

    def choose_category(self):
        print("Choose a category:")
        categories = list(self.questions.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}) {category}")
        while True:
            choice = input("Enter the number of the category: ")
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            else:
                print("Invalid choice. Please select a valid category.")

    def add_question(self):
        category = input("Enter the category for your question: ")
        question = input("Enter your question: ")
        options = []
        for i in range(4):
            option = input(f"Enter option {chr(65+i)}: ")
            options.append(f"{chr(65+i)}) {option}")
        answer = input("Which option is the correct answer? (A/B/C/D): ").upper()
        
        if category not in self.questions:
            self.questions[category] = []
        self.questions[category].append({
            "question": question,
            "options": options,
            "answer": answer
        })
        print("\nYour question has been added successfully!\n")

    def display_question(self, question_data, question_number):
        print(f"Question {question_number}: {question_data['question']}")
        for option in question_data["options"]:
            print(option)

    def get_user_input(self):
        while True:
            user_input = input("Your answer (A/B/C/D): ").upper()
            if user_input in ["A", "B", "C", "D"]:
                return user_input
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def give_feedback(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("🎉 Correct!\n")
            return True
        else:
            print(f"❌ Incorrect! The correct answer was {correct_answer}.\n")
            return False

    def run_quiz(self):
        self.display_banner("Welcome to the Quiz Game!")
        while True:
            print("1) Start Quiz")
            print("2) Add a Question")
            print("3) Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                category = self.choose_category()
                questions = random.sample(self.questions[category], len(self.questions[category]))
                for index, question_data in enumerate(questions):
                    self.display_question(question_data, index + 1)
                    user_answer = self.get_user_input()
                    if self.give_feedback(user_answer, question_data["answer"]):
                        self.score += 1
                self.display_final_score()
                break
            elif choice == "2":
                self.add_question()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_final_score(self):
        print(f"\nQuiz Completed! 🎉 Your final score is {self.score}/{sum(len(q) for q in self.questions.values())}\n")
        self.display_banner("Thank you for playing!")


if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.run_quiz()
