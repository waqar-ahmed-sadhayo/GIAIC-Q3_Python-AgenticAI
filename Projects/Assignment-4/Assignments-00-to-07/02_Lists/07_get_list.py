# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def main():
    lst = []
    element = input("Enter a value: ")
    while element != "":
        lst.append(element)
        element = input("Enter a value: ")
    print(lst)

if __name__ == "__main__":
    main()
