char = input("Enter a single character: ")

# Validate that the user entered exactly one character
if len(char) == 1:
    # Check if the character is a digit
    if char.isdigit():
        print(f"'{char}' is a number.")
    else:
        print(f"'{char}' is not a number.")
else:
    print("Please enter exactly one character.")