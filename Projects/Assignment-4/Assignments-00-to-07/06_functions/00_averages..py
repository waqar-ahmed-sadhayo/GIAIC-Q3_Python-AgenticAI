# Write a function that takes two numbers and finds the average between the two.

def average(a:float, b:float):
    sum = a + b
    return sum / 2

def main():
    num1_average = average(5,5)
    num2_average = average(2, 4)
    final_average = average(num1_average, num2_average)

    print(f"Average1: {num1_average}")
    print(f"Average2: {num2_average}")
    print(f"Final Average: {final_average}")

if __name__ == "__main__":
    main()
