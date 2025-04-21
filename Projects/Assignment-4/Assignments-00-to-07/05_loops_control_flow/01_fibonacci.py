# Write a program to print terms in the Fibonacci sequence up to a maximum value.

MAX_TERM_VALUE = 10000

def main():
    current_num = 0
    next_num = 1

    while current_num <= MAX_TERM_VALUE:
        print(current_num, end=" ")
        term_after_next_num = current_num + next_num
        current_num = next_num
        next_num = term_after_next_num



if __name__ == "__main__":
    main()