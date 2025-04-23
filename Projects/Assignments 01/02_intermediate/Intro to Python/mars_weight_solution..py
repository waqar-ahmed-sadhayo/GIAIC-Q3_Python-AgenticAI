def main():
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupyter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }


    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a Planet: ")

    if planet in planet_gravity:
        planet_weight = round(earth_weight * planet_gravity[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

if __name__ == "__main__":
    main()
