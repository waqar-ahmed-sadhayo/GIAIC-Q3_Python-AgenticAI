

BOLD = '\033[1m'
ITALIC = '\033[3m'
RESET = '\033[0m'

def num_in_stock(fruit: str):
    if fruit == 'apple':
        return 2
    if fruit == 'banana':
        return 5
    if fruit == 'mango':
        return 100
    if fruit == 'pear':
        return 1000
    if fruit == 'durian':
        return 4
    else:
        return 0

def main():
    fruit = input("Enter a fruit: ")
    print(f"{BOLD}{ITALIC}{fruit}{RESET}")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock." )
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == "__main__":
    main()