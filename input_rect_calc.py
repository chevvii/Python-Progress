# A function that prompts the user to enter data in string

# Rectangle Area Calculator
unit = input("Enter the unit measurement: ")
length = float(input("Enter the length value: "))
width = float(input("Enter the width value: "))

area = length * width
print(f"The Area of a {length} {unit} by {width} {unit} rectangle is {area} {unit}².")