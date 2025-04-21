# Guess My Number!

import  random
target_number = random.randint(1,99)


while True:
    user_input = input("Enter your number or press enter to exit: ")

    if user_input == "":
        print("Game Exited!")
        break

    try:
        user_number = int(user_input)
    except ValueError:
        print("Enter please enter a valid number")
        continue

    if user_number > target_number:
        print("Your guess is to high!")
    elif user_number < target_number:
        print("Your guess is to low!")
    else:
        print(f"Congrats! the number was {user_number}")
        break


