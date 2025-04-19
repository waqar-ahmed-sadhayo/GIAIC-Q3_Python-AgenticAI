# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_number(num_list):
    total = 0
    for num in num_list:
        total = total + num

    return total

def main():
    list_range = int(input("Enter the range of list: "))
    num_list = []
    for i in range(list_range):
        i = int(input())
        num_list.append(i)
    print(num_list)

    total = add_number(num_list)
    print(f"The sum of list number is: {total}")

if __name__ == "__main__":
    main()