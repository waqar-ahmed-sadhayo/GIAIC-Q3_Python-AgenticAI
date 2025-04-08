# Ask the user for a number and print its square (the product of the number times itself).

def main():
    number = float(input("\033[1;3mType a number to see its square: "))
    number_square = number ** 2
    print(f"{number} Squared is {number_square}")

if __name__ == "__main__":
    main()