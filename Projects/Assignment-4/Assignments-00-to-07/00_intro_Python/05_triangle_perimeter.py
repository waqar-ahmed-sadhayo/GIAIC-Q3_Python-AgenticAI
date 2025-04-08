# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def main():
    side1 = float(input("\033[1;3mWhat is the length of side 1: "))
    side2 = float(input("\033[1;3mWhat is the length of side 2: "))
    side3 = float(input("\033[1;3mWhat is the length of side 3: "))

    perimeter_of_triangle = side1 + side2 + side3
    print(f"The Perimeter of Triangle is: {perimeter_of_triangle}")

if __name__ == "__main__":
    main()
