import random
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("400x300")
        
        self.score = 0
        self.correct_count = 0
        self.incorrect_count = 0
        self.question_number = 0
        self.num1 = 0
        self.num2 = 0
        self.operation = ''
        self.difficulty = 1
        
        # Initialize main menu
        self.display_main_menu()
    
    def display_main_menu(self):
        self.clear_window()
        
        tk.Label(self.root, text="Select Difficulty Level", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Easy (Single Digits)", command=lambda: self.start_quiz(1)).pack(pady=5)
        tk.Button(self.root, text="Moderate (Double Digits)", command=lambda: self.start_quiz(2)).pack(pady=5)
        tk.Button(self.root, text="Advanced (Four Digits)", command=lambda: self.start_quiz(3)).pack(pady=5)
        
    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.correct_count = 0
        self.incorrect_count = 0
        self.question_number = 0
        self.ask_question()
    
    def ask_question(self):
        if self.question_number < 10:
            self.question_number += 1
            self.num1 = self.generate_random_number()
            self.num2 = self.generate_random_number()
            self.operation = self.decide_operation()
            
            self.clear_window()
            question_text = f"Question {self.question_number}: {self.num1} {self.operation} {self.num2} = ?"
            tk.Label(self.root, text=question_text, font=("Arial", 14)).pack(pady=10)
            
            self.answer_entry = tk.Entry(self.root)
            self.answer_entry.pack(pady=5)
            
            tk.Button(self.root, text="Submit", command=self.check_answer).pack(pady=10)
        else:
            self.display_results()
    
    def generate_random_number(self):
        if self.difficulty == 1:
            return random.randint(1, 9)
        elif self.difficulty == 2:
            return random.randint(10, 99)
        elif self.difficulty == 3:
            return random.randint(1000, 9999)
    
    def decide_operation(self):
        return random.choice(['+', '-'])
    
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            correct_answer = self.num1 + self.num2 if self.operation == '+' else self.num1 - self.num2
            
            if user_answer == correct_answer:
                self.score += 10
                self.correct_count += 1
                messagebox.showinfo("Result", "Correct!")
            else:
                self.score += 5 if messagebox.askretrycancel("Incorrect", "Try again?") else 0
                if user_answer == correct_answer:
                    self.correct_count += 1
                else:
                    self.incorrect_count += 1
                    messagebox.showinfo("Answer", f"Incorrect. The correct answer was {correct_answer}.")
            
            self.ask_question()
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid integer.")
    
    def display_results(self):
        self.clear_window()
        
        tk.Label(self.root, text="Quiz Results", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Final Score: {self.score}/100", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.root, text=f"Correctly Answered: {self.correct_count}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Incorrectly Answered: {self.incorrect_count}", font=("Arial", 12)).pack()
        
        grade = self.get_grade()
        tk.Label(self.root, text=f"Grade: {grade}", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Button(self.root, text="Play Again", command=self.display_main_menu).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=5)
    
    def get_grade(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "D"
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Start the quiz app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
