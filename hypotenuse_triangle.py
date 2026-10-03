import math

unit_measurement = input("Enter the unit measurement: ")
a = float(input("Enter side A value: "))
b = float(input("Enter side B value: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse is: {round(hypotenuse, 2)} {unit_measurement}")