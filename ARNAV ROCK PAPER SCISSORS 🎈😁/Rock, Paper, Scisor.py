import random

while True:
    print("\n")
    print("1) Rock 🪨")
    print("2) Paper 📄")
    print("3) Scissor ✂")
    selection = int(input("Enter Throw: "))

    if selection == 1:
        player_throw = "Rock"
    elif selection == 2:
        player_throw = "Paper"
    else:
        player_throw = "Scissor"

    print("\n")
    print("Player Throws", player_throw)

    throws = ["Rock", "Paper", "Scissor"]
    ai_throw = random.choice(throws)

    print("AI throws:", ai_throw)

    if player_throw == ai_throw:
        print("Tie!")
    elif player_throw == "Rock":
        if ai_throw == "Paper":
            print("You lose, better luck next time 🤷🤷!")
        elif ai_throw == "Scissor":
            print("Congrats! bet you won't win again 🥳🥳 ")
    elif player_throw == "Scissor":
        if ai_throw == "Paper":
            print("Congrats! bet you won't win again 🥳🥳")
        elif ai_throw == "Rock":
            print("You lose, better luck next time! 🤷🤷")
    elif player_throw == "Paper":
        if ai_throw == "Rock":
            print("Congrats! bet you won't win again 🥳🥳")
        elif ai_throw == "Scissor":
            print("You lose, better luck next time! 🤷🤷")

    print("\n")
    print("1, Play Again")
    print("2, Quit")
    selection = int(input("Enter Choice:"))

    if (selection == 2):
        break

        
        
        
    
        
