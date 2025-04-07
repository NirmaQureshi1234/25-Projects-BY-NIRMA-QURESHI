import random

print("Welcome to Your Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?1234567890'

number = input("How many letters would you like in your password? ")
number = int(number)

length =input('Input the length of the password: ')
length = int(length)

print('\nhere are your passwords: ')   

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)