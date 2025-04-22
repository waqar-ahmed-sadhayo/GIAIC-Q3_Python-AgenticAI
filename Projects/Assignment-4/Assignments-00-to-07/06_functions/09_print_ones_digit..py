# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

BLUE = '\033[94m'
RESET = '\033[0m'

def print_ones_digit(num):
    print(f"The Ones digit is: {num % 10}")

def main():
    num = int(input("Enter a number: "))
    print(f"You Entered: {BLUE}{num}{RESET}")
    print_ones_digit(num)

if __name__ == "__main__":
    main()