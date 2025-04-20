

# simple Function
MINIMUM_HEIGHT = 50
def main():
    height_input = int(input('\033[1;3m' + "How tall are you? " + '\033[0m'))
    if height_input >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()


# Extra Challenge Function Code
def tall_enough_extension():
    minimum_height = 50

    while True:
        height_input = input("How tall are you? ")

        if not height_input:  # If the user hits enter without typing anything
            print("Exiting the ride checker. Have a great day!")
            break

        try:
            height = int(height_input)
            if height >= minimum_height:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# Run the extended function
tall_enough_extension()
