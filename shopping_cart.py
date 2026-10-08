# Shopping cart program

groceries = []
prices = []
quantities =[]
total = 0
x = 0

print("Welcome to our store!")
currency = input("To start with, enter your currency: ")

while currency.isdigit() or not currency:
	if currency.isdigit():
		print("Currency can not be numbers.")
	else:
		print("Currency can not be empty.")
	currency = input("To start with, enter your currency: ")

while True:
	grocery = input("Enter your grocery (q if done): ")
	if not grocery:
		print("Grocery can not be empty.")
		continue
	if grocery.lower() == "q":
		break

	while True:
		price = input(f"Enter the price for {grocery}(enter if there is no price): ")

		if price == "":
			price = 0
			break

		else:
			try:	
				price = float(price)
				if price <  0:
					print("Price can not be negative.")
					continue
				break
			except ValueError:
				print("Price can only contain numbers.")

	while True:
		quantity = input(f"Enter the quantity for {grocery}(enter if there is only one item): ")

		if quantity == "":
			quantity = 1
			break
		else:
			try:	
				quantity = int(quantity)
				if quantity <=  0:
					print("quantity can not be zero or negative.")
					continue
				break
			except ValueError:
				print("Quantity can only contain numbers.")

	groceries.append(grocery)
	prices.append(price)
	quantities.append(quantity)

for i in range(len(groceries)):
	print(f"{quantities[i]}x {groceries[i]} = {prices[i] * quantities[i]:.2f} ({prices[i]:.2f} for each.)")
	total += prices[i] * quantities[i]

print(f"Your total price is: {total:,.2f} with total of {sum(quantities)} item(s)")
print("Thank you for your shopping!")