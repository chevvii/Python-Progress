import math

# x = 3.14
# y = -1
# z = 49

# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max(x, y, z)
# result = min(x, y, z)

# print(result)

# print(math.pi)
# print(math.e)
# result = math.sqrt(z)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

# Circumference of a circle
unit_measurement = input("Enter the unit measurement: ")
radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)} {unit_measurement}")