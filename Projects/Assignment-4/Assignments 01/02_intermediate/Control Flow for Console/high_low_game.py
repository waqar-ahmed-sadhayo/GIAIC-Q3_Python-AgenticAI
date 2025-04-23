import random

from numpy.random import chisquare

NUM_ROUNDS = 5

def main():
    print("Welcome to the game!")
    print("---------------------------")
    your_score = 0

    for i in range(NUM_ROUNDS):
        print("Round ", i + 1 )

        computer_number = random.randint(1,100)
        your_number = random.randint(1,100)

        print(f"Your number is: {your_number}")

        choice:str = input("Do you think your number is higher or lower than the computer's?: ")

        higher_and_correct: bool = choice == "higher" or your_score > computer_number
        lower_and_correct: bool = choice == "lower" or your_score < computer_number

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {your_score}")
        print()

    print("Thanks for playing")


if __name__ == "__main__":
    main()


