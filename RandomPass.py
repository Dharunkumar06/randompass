import random
import string

def generate_pass(len, use_upper, use_lower, use_digits, use_special_ch, special_ch):
    # Define character sets
    ch = ""
    if use_upper:
        ch += string.ascii_uppercase
    if use_lower:
        ch += string.ascii_lowercase
    if use_digits:
        ch += string.digits
    if use_special_ch:
        ch += special_ch
    
    if not ch:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(ch) for _ in range(len))
    return password


print("******Random Password Generator******")

len = int(input("Enter the desired password length: "))
    
use_upper = input("If You Want To Include uppercase letters? (yes/no): ").lower() == "yes"
use_lower = input("If You Want To Include lowercase letters? (yes/no): ").lower() == "yes"
use_digits = input("If You Want To Include digits? (yes/no): ").lower() == "yes"
    
use_special_ch = input("Include special characters? (yes/no): ").lower() == "yes"
special_ch = string.punctuation if use_special_ch else ""

password = generate_pass(len, use_upper, use_lower, use_digits, use_special_ch, special_ch)
    
if password:
    print("Generated Password:", password)


