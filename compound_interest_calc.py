# I know I can use function for more efficient algorithm, but I haven't learned it yet.

principle = 0
rate = 0
time = 0

while principle <= 0:
	try:
		principle = float(input("Enter the principle amount: "))
		if principle <= 0:
			print("Principle can't be less than or equal to zero.")

	except ValueError:
		print("Principle can only contain numbers.")


while rate <= 0:
	try:
		rate = float(input("Enter the interest rate amount: "))
		if rate <= 0:
			print("Interest rate can't be less than or equal to zero.")

	except ValueError:
		print("Interest rate can only contain numbers.")


while time <= 0:
	try:
		time = int(input("Enter the time duration (Years): "))
		if time <= 0:
			print("Time can't be less than or equal to zero.")

	except ValueError:
		print("Time can only contain numbers.")


total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")