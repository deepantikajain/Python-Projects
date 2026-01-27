import random
import string

print("===== ADVANCED PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
use_digits = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = ""

if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("❌ You must select at least one character type!")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
