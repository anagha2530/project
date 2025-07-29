from time import sleep

def countdown(n):
    print(n)
    sleep(0.5)

    if n == 1:
        return 
    else:
        countdown(n-1)
    
n = int(input("enter the number : "))
countdown(n)