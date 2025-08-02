
                      # rock, paper ,secsisor
import numpy as np

opt = ["Rock", "Paper", "Scissor"]
print('Welcome to my game (Rock, Paper, Scissor)!')

while True:
    try:
        user_choice = input("Enter your guess: ").capitalize()

        if user_choice not in opt:
            print("Invalid choice, try again!")
            continue  # This was misplaced in your code

        comp_choice = np.random.choice(opt)

        print(f"Computer 💻 chooses: {comp_choice}")
        print(f"Hiba chooses: {user_choice}")

        if comp_choice == user_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and comp_choice == "Scissor") or \
                (user_choice == "Paper" and comp_choice == "Rock") or \
                (user_choice == "Scissor" and comp_choice == "Paper"):
            print("You win! 🎉")
        else:
            print("You lose 😢")

    except Exception as e:
        print("An error occurred:", e)

