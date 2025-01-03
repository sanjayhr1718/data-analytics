import tkinter as tk
from tkinter import messagebox

# Sample quiz data (questions, options, and answers)
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "What is the square root of 16?", "options": ["2", "4", "8", "16"], "answer": "4"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Quiz Application")
        self.root.geometry("500x400")
        
        # Initializing variables
        self.current_question = 0
        self.score = 0
        
        # Display first question
        self.display_question()

    def display_question(self):
        # Clear previous question content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Get current question and options
        question_data = questions[self.current_question]
        question_text = question_data["question"]
        options = question_data["options"]

        # Display question text
        question_label = tk.Label(self.root, text=question_text, font=("Arial", 14))
        question_label.pack(pady=20)

        # Display options as buttons
        self.var = tk.StringVar()
        self.var.set(None)  # Initialize to no selection

        for option in options:
            option_button = tk.Radiobutton(self.root, text=option, variable=self.var, value=option, font=("Arial", 12))
            option_button.pack(pady=5)

        # Next button
        next_button = tk.Button(self.root, text="Next", command=self.check_answer, font=("Arial", 12))
        next_button.pack(pady=20)

    def check_answer(self):
        # Get the selected answer
        selected_answer = self.var.get()

        # Check if the selected answer is correct
        correct_answer = questions[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1

        # Move to the next question
        self.current_question += 1

        # Check if there are more questions
        if self.current_question < len(questions):
            self.display_question()
        else:
            self.show_results()

    def show_results(self):
        # Display the result when the quiz is over
        messagebox.showinfo("Quiz Over", f"Your score: {self.score} out of {len(questions)}")
        self.root.quit()

# Create the main window and pass it to the QuizApp class
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
