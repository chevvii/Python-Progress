import math

unit_measurement = input("Enter the unit measurement: ")
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)} {unit_measurement}^2")