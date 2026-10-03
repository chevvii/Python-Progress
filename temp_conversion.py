unit1 = input("Enter the unit of temperature (C/F/K): ")
temp = float(input("Enter the value of the temperature in the following unit: "))
unit2 = input("Enter the unit of temperature to convert into (C/F/K): ")
decimal = int(input("Enter how many decimal would you like: "))

if unit1 == "C" and unit2 == "F":
	result = temp * (9/5) + 32
	print(f"The temperature of {temp} {unit1} converted into {unit2} is: {round(result, decimal)} {unit2} ")

elif unit1 == "C" and unit2 == "K":
	result = temp + 273.15
	print(f"The temperature of {temp} {unit1} converted into {unit2} is: {round(result, decimal)} {unit2} ")

elif unit1 == "K" and unit2 == "C":
	result = temp - 273.15
	print(f"The temperature of {temp} {unit1} converted into {unit2} is: {round(result, decimal)} {unit2} ")

elif unit1 == "F" and unit2 == "C":
	result = (temp - 32) * (5/9)
	print(f"The temperature of {temp} {unit1} converted into {unit2} is: {round(result, decimal)} {unit2} ")

elif unit1 == "F" and unit2 == "K":
	result = (temp - 32) * (5/9) + 273.15
	print(f"The temperature of {temp} {unit1} converted into {unit2} is: {round(result, decimal)} {unit2} ")

else:
	print("unit can't be the same or it is invalid.")

