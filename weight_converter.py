unit = input("Enter weight measuring unit (KG / lbs): ")
weight = float(input("Enter your weight in the following unit: "))
decimal = int(input("How many decimal would you prefer: "))

if unit == "KG":
	weight = weight * 2.205
	unit = "lbs"
	print(f"Your weight in {unit} is: {round(weight, decimal)} {unit}")
	
elif unit == "lbs":
	weight = weight / 2.205
	unit = "KG"
	print(f"Your weight in {unit} is: {round(weight, decimal)} {unit}")

else:
	print(f"{unit} was not valid.")
