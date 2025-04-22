
BOLD = '\033[1m'
ITALIC = '\033[3m'
RESET = '\033[0m'

def greet(name):
    return "Greetings " + name

def main():
    name = input("What's your name? ")
    print(f"{BOLD}{ITALIC}{name}{RESET}")
    print(greet(name))

if __name__ == "__main__":
    main()