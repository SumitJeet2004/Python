quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "Which element has the chemical symbol 'O'?", "answer": "Oxygen"}
]

# Initialize the prize amount
prize_per_question = 10000000  # 1 crore in smallest denomination
total_prize = 0

# Function to run the quiz
def run_quiz():
    global total_prize
    print("Welcome to the Quiz Game! Each correct answer wins you 1 crore.")
    
    for item in quiz:
        print(item["question"])
        answer = input("Your answer: ")
        
        if answer.strip().lower() == item["answer"].strip().lower():
            print("Correct!")
            total_prize += prize_per_question
        else:
            print(f"Wrong! The correct answer is {item['answer']}.")
    
    print(f"Your total prize amount is: {total_prize / 10000000} crore.")


run_quiz()