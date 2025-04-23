# Print 10 random numbers in the range 1 to 100.
import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_Value = 100

def main():
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_Value), end=" ")

if __name__ == "__main__":
    main()

