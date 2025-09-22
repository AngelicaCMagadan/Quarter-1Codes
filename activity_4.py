full_name = input("Enter your full name (First, Middle, Last): ")
names = [name.strip() for name in full_name.split(",")]

firstname = names[0].capitalize()
middlename = names[1].capitalize()
lastname = names[2].capitalize()

middle_initial = middlename[0] + "."

format_name = f"{lastname}, {firstname} {middle_initial}"

print("Formatted name: ", format_name)