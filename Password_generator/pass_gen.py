import random
import string
import pyperclip

def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("===== Advanced Password Generator =====")

while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

digits = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, digits, symbols)

print("\nGenerated Password:")
print(password)

pyperclip.copy(password)

print("\nPassword copied to clipboard successfully!")