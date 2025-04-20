# Check whether the year is Leap Year or not.

def main():
    year = int(input("Enter a Year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a Leap Year")
            else:
                print(f"{year} is not a Leap Year")
        else:
            print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

if __name__ == "__main__":
    main()