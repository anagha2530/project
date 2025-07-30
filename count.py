from time import sleep

def countdon(n):
    print(n)
    sleep(0.5)

    if n == 1:
        return 
    else:
        countdon(n-1)
    
n = int(input("enter the number : "))
countdon(n)