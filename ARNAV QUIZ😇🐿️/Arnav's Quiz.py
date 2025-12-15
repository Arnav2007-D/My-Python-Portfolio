print("Welcome to Arnav's Quiz 🥳🥳")
print("Lets get Started!")

questions = (
    "Why does Arnav want to pursue Computer Science?:",
    "What is Arnav's favourite fast food chain?:",
    "How long did it take for Arnav to make this project?:",
    "Who is Arnav's favourite music artist?:",
    "What does Arnav want to do in life?:"
)

options = (
    ("A. He finds coding fun and calming", "B. It sounds cool", "C. He doesnt know"),
    ("A. Hungry Jack", "B. Pizza Hut", "C. Guzman y Gomez"),
    ("A. 2 Days", "B. 20 minutes", "C. 45 minutes"),
    ("A. Tame Impala", "B. Kendrick Lamar", "C. Childish Gambino"),
    ("A. Start a tech startup", "B. Help out his cousins with their struggles", "C. All the above")
)

answers = ("A", "C", "B", "B", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    # Input validation loop
    while True:
        guess = input("Enter A, B, or C: ").upper()
        if guess in ("A", "B", "C"):
            break
        print("Please enter A, B, or C only!")

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("✅ CORRECT!")
    else:
        print("❌ INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1

print("------------------")
print("RESULTS")
print("------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percent = int((score / len(questions)) * 100)
print(f"Your score is {score_percent}%")

if score_percent == 100:
    print("🌺WE NEED TO BE FRIENDS ASAP🌺")
elif score_percent >= 80:
    print("Great job! we would be good friends someday 😊")
else:
    print("Close enough, try again!!")
