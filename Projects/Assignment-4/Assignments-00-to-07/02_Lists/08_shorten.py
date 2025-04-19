# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)

def get_lst():
    lst = []
    element = input("Please enter an element of the list or press enter to exit: ")
    while element != "":
        lst.append(element)
        element = input("Please enter an element of the list or press enter to exit: ")

    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == "__main__":
    main()

