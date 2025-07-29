import random
n = input("enter the name of the user: ")

words = ['carbon','dioxide','hydrogen','water','computer','science','engine','diode','dice','die',]

word = random.choice(words)
print("guess the character")
guess = ' '
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char,end = '')