import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

print("password generator")

nr_letters = int(input("enter the no of letters: "))
nr_numbers = int(input("enter the no of numbers: "))
nr_symbols = int(input("enter the no of symbols: "))

password = []

for i in range(nr_letters):
    password.append(letters[random.randint(0,len(letters))])
for i in range(nr_numbers):
    password.append(numbers[random.randint(0,len(numbers))])
for i in range(nr_symbols): 
    password.append(symbols[random.randint(0,len(symbols))])

random.shuffle(password)
passwords = ''
for i in password:
    passwords += i
print(passwords)