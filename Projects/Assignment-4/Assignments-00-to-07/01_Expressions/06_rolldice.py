# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

Num_sides: int = 6
def main():
    dice1:int = random.randint(1, Num_sides)
    dice2:int = random.randint(1, Num_sides)

    total = dice1 + dice2

    print(f"Result of Dice 1 is: ", dice1)
    print(f"Result of Dice 2 is: ", dice2)
    print(f"Total of {dice1} and {dice2} is: ", total)

if __name__ == "__main__":
    main()
