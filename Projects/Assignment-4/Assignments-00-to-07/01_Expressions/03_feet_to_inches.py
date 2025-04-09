# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

inches_in_foot = 12
def main():
    feet = float(input("Enter the feet: "))
    feet_to_inches = feet * 12

    print(f"{feet} Feet is equal to {feet_to_inches} inches!")

if __name__ == "__main__":
    main()