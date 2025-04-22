def count_even_list(lst):
    count = 0
    for num in lst:
        if num %2 == 0:
            count += 1

    print(count)

def get_list_of_ints():
    lst = []
    user_input = input("Enter an integer or press enter to exit!: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to exit!: ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even_list(lst)

if __name__ == "__main__":
    main()


