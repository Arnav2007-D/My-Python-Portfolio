import random

def choose_city():
    cities = ['bangkok', 'london','mecca ', 'dubai', 'paris',
    'tokyo', 'rome', 'milan','beijing', 'amsterdam', 
    'sydney', 'singapore ', 'barcelona']
    return random.choice(cities) 


def city_status(city, guessed_letters):
    display = ""
    for letter in city:
        if letter in guessed_letters:
            display += letter
        else:
            display += " _ "
    return display

def city_guessing_game():
    secret_city = choose_city()
    guessed_letters = []
    attempts = 5

    print("City Guessing Game!😃😃")
    print("******************")
    print("Secret City 🤔:", city_status(secret_city, guessed_letters))

    while attempts > 0:

        guess = input("Guess A letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed this letter")
            continue
        guessed_letters.append(guess)

        if guess not in secret_city:
            attempts -= 1
            print(f"No letter '{guess}' occurs in the word.")
            print(f"You have '{attempts}' attempts left")
        else:
            occurrences = secret_city.count(guess)
            print(f"Letter '{guess}' occurs {occurrences} times.")

        current_status = city_status(secret_city, guessed_letters)
        print("Secret_city:", current_status)

        if " _ " not in current_status:
            print("🎉🎉 Congratulations! You guessed the City🗼🗼.")
            input("Press Enter to exit the game...")
            break

    if attempts == 0:
        print(f"You ran out of attempts 😞😞! The City was {secret_city}")
        input("Press Enter to exit the game...")

city_guessing_game()

