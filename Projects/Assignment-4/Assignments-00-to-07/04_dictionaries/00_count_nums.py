# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def get_user_number():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)

    return user_numbers


def count_nums(num_list):
    num_dict = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(num, " appears ", num_dict[num], " times.")

def main():
    user_numbers = get_user_number()
    num_list = count_nums(user_numbers)
    print_counts(num_list)

if __name__ == "__main__":
    main()