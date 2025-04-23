import random
def main():
    secret_number: int = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    guess_number = int(input("Enter a guess: "))

    while guess_number != secret_number:
        if guess_number < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is to high")

        print()
        guess_number = int(input("Enter a new number: "))

    print(f"Congrats! The number was: {guess_number}")


if __name__ == "__main__":
    main()

