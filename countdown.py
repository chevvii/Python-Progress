import time

while True:

	my_time = input("Enter the time in seconds: ")

	if my_time.isdigit():
		my_time = int(my_time)
		print(f"The countdown will be set to {my_time} second(s).")
		start = input("Start? (Y/N(reset)): ").strip().upper()

		if start == "Y":
			for x in range(my_time, 0, -1):

				second = x % 60
				minute = int(x / 60) % 60
				hour = int(x / 3600)

				print(f"{hour:02}:{minute:02}:{second:02}")
				time.sleep(1)

			print("Time is up!")
			end = input("Would you like to do another countdown? (Y/N): ").strip().upper()

			if end == "Y":
				continue

			else:
				break
				
		else:
			continue

	else:
		print("Please enter only number.")
		continue
	
print("Thank you for using our countdown!")