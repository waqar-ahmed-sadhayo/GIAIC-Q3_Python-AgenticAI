# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

def main():
    my_list = [1,2,3,4]
    for i in range(len(my_list)):
        elem_at_index = my_list[i]
        my_list[i] = elem_at_index * 2
    print(my_list)


if __name__ == "__main__":
    main()

