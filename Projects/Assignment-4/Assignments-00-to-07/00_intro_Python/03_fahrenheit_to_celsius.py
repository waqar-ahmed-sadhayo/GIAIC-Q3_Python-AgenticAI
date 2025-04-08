# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

def main():
    temperature_in_fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
    temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature {temperature_in_fahrenheit}F = {temperature_in_celsius}")

if __name__ == "__main__":
    main()