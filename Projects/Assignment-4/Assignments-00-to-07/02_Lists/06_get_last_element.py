def get_last_element(lst):
    print(lst[-1])

def get_list():
    lst = []
    element = input("Please enter a element or press enter to exit: ")
    while element != "":
        lst.append(element)
        element = input("Please enter a element or press enter to exit: ")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)

if __name__ == "__main__":
    main()