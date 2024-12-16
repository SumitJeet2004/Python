# List of questions and their correct answers
quiz = [
    ("ehat is namne of PM", "Modi"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("what is mandatory", "money"),
    ("What is the smallest prime number?", "2"),
    ("Which element has the chemical symbol 'O'?", "Oxygen")
]

# Initialize the prize amount
prize_per_question = 1  # 1 crore per correct answer
total_prize = 0

# Function to run the quiz
def run_quiz():
    global total_prize
    print("Welcome to the Quiz Game! Each correct answer wins you 1 crore.")
    
    for question, correct_answer in quiz:
        print(question)
        answer = input("Your answer: ")
        
        if answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            total_prize += prize_per_question
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    print(f"Your total prize amount is: {total_prize} crore.")


run_quiz()
