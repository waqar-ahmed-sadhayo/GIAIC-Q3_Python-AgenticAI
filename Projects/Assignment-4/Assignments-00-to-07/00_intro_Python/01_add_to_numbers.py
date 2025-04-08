# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    total = num1 + num2
    print(f"The Sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main()