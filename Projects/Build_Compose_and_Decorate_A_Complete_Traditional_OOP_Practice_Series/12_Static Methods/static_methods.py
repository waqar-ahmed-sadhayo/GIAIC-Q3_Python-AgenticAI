class TemperatureConvertor:

    @staticmethod  
    def celsius_to_fahrenheit(celsius):  # Static Method
        return (celsius * 9/5) + 32


temp_celsius = 25

# Call the static method using the class name to convert to Fahrenheit
temp_fahrenheit = TemperatureConvertor.celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")