# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
#
# For example if the user enters the number 2 you would then print:
#
# 4 8 16 32 64 128

def main():
    current_number = input("Please enter the number or press enter to exit: ")
    while int(current_number) <= 100:
        if current_number == "":
            break
        try:
            current_number = int(current_number)
        except ValueError:
            print("Invalid Value!, please enter a valid number")
        else:
            current_number *= 2
        print(current_number, end=" ")


if __name__ == "__main__":
    main()
