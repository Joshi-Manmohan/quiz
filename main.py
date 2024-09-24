# Python Quiz game

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Ostrich", "B. Elephant", "C. Hen", "D. Whale"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "D. Hydrogen"),
    ("A. 236", "B. 207", "C. 201", "D. 206"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "A", "B", "D", "B")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("--------------------------")
print("     RESULT      ")
print("--------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int(score / len(questions) * 100)
print(f"Your score is: {score_percentage}%")
