# Python Programming Internship
# Roaa Fathi
# Last Submission Date: 5 Sep.
# Random Password generator Application

import random
import string


# Generates passwords contains letters, digits and special characters
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Displays the rules of creating password
def display_rules():
    print("============== Welcome to Generate Password APP ==============")
    print("** Rules of Strong Password: **")
    print("1. At least 8 letters.")
    print("2. Uppercase letters: A-Z.")
    print("3. Lowercase letters: a-z.")
    print("4. Numbers: 0-9.")
    print("5. Symbols: ~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/")

    print("\n")


# Controls the app and enables input
def password_generator():
    display_rules()
    while True:
        try:
            password_length = int(input("Enter the desired password length (to exit enter -1): "))
            if password_length < 0:
                print("\n** Thanks for using our App. **")
                break
            elif password_length < 8:
                print("Strong Password length should be at least 8.\n")
            else:
                password = generate_password(password_length)
                print("Generated Password:", password)

        except ValueError:
            print("Please enter a valid positive integer for the password length.\n")


password_generator()
