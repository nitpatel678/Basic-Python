'''
name = input("Enter your name ")

# Remove spaces in string
name = name.strip()

# Capitalize user'name
name = name.capitalize()

print(f"Hello,{name}")

'''


# Chaining functions together.

# name = input("Enter your name ")
#  # Remove spaces and capatilize
# name = name.strip().title()

# print(f"Hello, {name}")




''' Another method of CHAINING '''

# name = input("Enter your name ").strip().title()
#  # Now print
# print(f"Hello, {name}")


# Ask user for their name
name = input("Enter your name ").strip().title()

# Split users name into first and last name
first , last = name.split()

# Say Hello to user 

print(f"hello, {first}")