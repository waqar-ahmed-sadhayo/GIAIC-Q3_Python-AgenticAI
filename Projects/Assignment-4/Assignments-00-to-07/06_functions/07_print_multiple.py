# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.


# ANSI color codes
BLUE = "\033[94m"
RESET = "\033[0m"

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message, end=" ")

def main():
    message: str = input("Please type a message: ")
    print(f"You typed: {BLUE}{message}{RESET}")  # Show the input in blue
    try:
        repeats: int = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)
    except ValueError:
        print("Please enter a valid number.")

main()
