# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    fruits = {
        "apple": 1.5,
        "durian": 50,
        "jackfruit": 80,
        "kiwi": 1,
        "rambutan": 1.5,
        "mango": 5
    }

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many ("+ fruit_name +") do you want? "))
        total_cost += (price * amount_bought)

    print(f"Your total is ${total_cost}")


if __name__ == "__main__":
    main()