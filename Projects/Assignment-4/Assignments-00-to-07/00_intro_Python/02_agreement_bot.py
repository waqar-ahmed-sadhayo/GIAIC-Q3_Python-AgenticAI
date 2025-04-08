# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():
    favorite_animal = input("\033[1;3m What's your favorite Animal___? ")
    print(f"My favorite Animal is also {favorite_animal}!")

if __name__ == "__main__":
    main()