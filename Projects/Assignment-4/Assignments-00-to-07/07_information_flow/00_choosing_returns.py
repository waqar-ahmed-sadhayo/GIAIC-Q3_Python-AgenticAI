
BOLD = '\033[1m'
ITALIC = '\033[3m'
RESET = '\033[0m'

ADULT_AGE: int = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("How old is this person: "))
    print(f"Your Age is: {BOLD}{ITALIC}{age}{RESET}")
    print(is_adult(age))

if __name__ == "__main__":
    main()
