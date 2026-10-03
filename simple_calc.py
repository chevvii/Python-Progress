print("=============================")
print("=     SIMPLE CALCULATOR     =")
print("=============================")

# Let user define
operation = input("Enter the operation (+, -, *, /): ")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
decimal = (input("How many decimal would you prefer to get? (skip for default = 2): "))

# in case user skipped
if decimal == "":
	decimal + "2" = int(decimal)
else:
	decimal = int(decimal
		)
if operation == "+":
	result = first_number + second_number
	print(f"{first_number} {operation} {second_number} = {round(result, decimal)}")

elif operation == "-":
	result = first_number - second_number
	print(f"{first_number} {operation} {second_number} = {round(result, decimal)}")

elif operation == "*":
	result = first_number * second_number
	print(f"{first_number} {operation} {second_number} = {round(result, decimal)}")

elif operation == "/":
	result = first_number / second_number
	print(f"{first_number} {operation} {second_number} = {round(result, decimal)}")

else:
	print("Please choose the right operation.")