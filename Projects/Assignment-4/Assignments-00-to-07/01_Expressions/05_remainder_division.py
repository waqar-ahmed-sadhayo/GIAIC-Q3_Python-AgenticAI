# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
from anaconda_project.internal.conda_api import result


def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to be divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"The result of division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()