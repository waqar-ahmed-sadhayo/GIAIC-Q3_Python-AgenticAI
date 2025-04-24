import random
import string

print("Welcome To Your Password Generator")

chars = string.ascii_letters + string.digits + string.punctuation

number = int(input("Amount of passwords to generate: "))

length = int(input("Input your password length: "))

print("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ' '
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)