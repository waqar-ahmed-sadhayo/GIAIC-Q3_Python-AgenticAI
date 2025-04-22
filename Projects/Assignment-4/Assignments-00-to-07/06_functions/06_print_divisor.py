# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!
from anyio import current_effective_deadline

def print_divisors(num: int):
    print(f"Here are the divisors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    try:
        user_input = input("Enter a number: ")
        if user_input.strip() == "":
            raise ValueError("Input cannot be empty.")
        user_input = int(user_input)
        if user_input <= 0:
            raise ValueError("Please enter a number greater than zero.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        print_divisors(user_input)

main()


if __name__ == "__main__":
    main()
