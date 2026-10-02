# Shopping Cart Progrm

item_name = input("What item would you like to buy?: ")
currency = input("What currency is the price?: ")
price = float(input("What is the price for each?: "))
quantity = float(input("How many would you like?: "))
total = price * quantity

print(f"You have bought: {quantity} x {item_name}")
print(f"Each price: {price} in {currency} currency")
print(f"Your total ({quantity}): {total} in {currency} currency")