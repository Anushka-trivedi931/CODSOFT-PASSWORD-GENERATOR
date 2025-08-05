import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for better security."

    # Character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure the password includes at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random characters
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the password list to randomize the order
    random.shuffle(password)

    return ''.join(password)

# --- Main Program ---
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")