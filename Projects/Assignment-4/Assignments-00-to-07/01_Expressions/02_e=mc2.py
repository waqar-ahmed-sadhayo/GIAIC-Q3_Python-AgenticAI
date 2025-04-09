# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

def main():
    mass_in_kg = float(input("Enter Mass in Kilograms: "))
    speed_of_light = 299792458
    energy_in_joules: float = mass_in_kg * (speed_of_light ** 2)

    print("e = m * C^2")
    print("m = ", mass_in_kg, "kg")
    print("C = ", speed_of_light, "m/s")
    print(f"{energy_in_joules} joules of energy!")

if __name__ == "__main__":
    main()
