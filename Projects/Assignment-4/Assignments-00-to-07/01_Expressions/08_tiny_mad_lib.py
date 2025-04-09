# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
SENTENCE_START = "You are my most beautiful"
BOLD = '\033[1m'
END = '\033[0m'
def main():
    adjective = str(input("Please type an adjective and press enter: "))  # Shining
    noun = str(input("Please type an noun and press enter: ")) # Star
    verb = str(input("Please type an input and press enter: ")) # glow

    print(f"{SENTENCE_START} {BOLD}{adjective}{END} {BOLD}{noun}{END} {BOLD}{verb}{END}")

if __name__ == "__main__":
    main()