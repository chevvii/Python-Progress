# Do some code only if the condition is true. Else, do something else lol

name =  input("Enter your name: ")
response = input("Want to check your age?(Y/N): ")

if response == "Y":
	age = int(input("Enter your age: "))
	
	if age >= 21:
		print(f"{name}, you are {age} years old, which mean that you're old enough to enter.")

	elif age >= 18:
		print(f"{name}, you are {age} years old, which mean that you're legally old enough, but still got rules to follow.")

	elif age <= 0:
		print("You haven't been born yet.")

	else:
		print(f"I'm sorry {name}, you are {age} years old, which mean that you're still prohibited from entering.")

else:
	print(f"Okay {name}, have a good day!")

