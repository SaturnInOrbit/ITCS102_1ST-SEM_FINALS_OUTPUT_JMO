def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)

print("Welcome to the temperature converter!")
print("Are you looking to convert Fahrenheit-to-Celcius or Celcius-to-Fahrenheit?")
print("\t\t[#1]Fahrenheit-to-Celcius")
print("\t\t[#2]Celcius-to-Fahrenheit")
num = int(input("Enter the number of your choice: "))
if num == 1:
    fahrenheit = float(input("Please enter temperature in Fahrenheit: "))
    print(f"The conversion of {fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C.")
elif num == 2:
    celsius = float(input("Please enter temperature in Celsius: "))
    print(f"The conversion of {celsius}°C is {celsius_to_fahrenheit(celsius)}°F.")
else:
    print("Huh")