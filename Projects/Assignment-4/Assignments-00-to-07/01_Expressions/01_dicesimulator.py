# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

Num_Sides = 6

def roll_dice():
    dice1 = random.randint(1, Num_Sides)
    dice2 = random.randint(1, Num_Sides)
    total = dice1 + dice2

    print(f"Dice 1: {dice1}, Dice 2: {dice2}, Total: {total}")

def main():
    dice1 = 10
    for _ in range(3):
        print(f"\033[1;3mDice 1 in main() is still {dice1}")
        roll_dice()

if __name__ == "__main__":
    main()