# Ask the user for their name
name = input("Enter your name: ")

# Ask for their birth year and convert it to an integer
birth_year = int(input("Enter your birth year: "))

# Calculate age (assuming current year is 2026)
current_year = 2026
age = current_year - birth_year

# Print a formatted message
print(f"Hello, {name}! You are turning {age} years old this year.")

