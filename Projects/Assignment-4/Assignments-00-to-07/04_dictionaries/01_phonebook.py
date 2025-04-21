# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_number():
    """Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook."""

    phone_book = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phone_book[name] = number

    return phone_book

def print_phone_book(phone_book):
    """Prints out all the names/numbers in the phonebook."""
    for name in phone_book:
        print(str(name), " -> ", str(phone_book[name]))


def lookup_numbers(phone_book):
    """Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name."""

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phone_book:
            print(name, " is not in the phonebook")
        else:
            print(phone_book[name])

def main():
    phone_book = read_phone_number()
    print_phone_book(phone_book)
    lookup_numbers(phone_book)

if __name__ == "__main__":
    main()