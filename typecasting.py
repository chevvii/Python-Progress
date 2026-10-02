# Typcasting = The process of converting a variable from one data type to another

name = "Ahmad Tsaqif M."
grade = 9
gpa = 3.02
graduation = "Graduated"

# Inline
print(f"We are declaring that: {name} from grade {str(grade)} with a GPA of {float(int(gpa))} is {graduation}.")

# Separated
grade = str(grade)
gpa = int(gpa)
gpa = float(gpa)
print(f"We are declaring that: {name} from grade {grade} with a GPA of {gpa} is {graduation}")

# Note that typecasting any other data type into boolean will ended up as a True, except if it's a blank variable
name = bool(name)
graduation = ""
graduation= bool(graduation)

print(name)
print(graduation)