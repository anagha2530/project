import random
while True:
    choice1 = input("enter the input(rock,paper,scissors): ")
    choice2 = input("enter the input(rock,paper,scissors): ")
    if choice1 == choice2:
        print("game over")
    elif(choice1 == "rock" and choice2 == "paper"):
        print("choice2 wins")
    elif(choice1 == "paper" and choice2 == "scissors"):
        print("choice2 wins")
    elif(choice1 == "scissors" and choice2 == "rock"):
        print("choice2 wins")
    else:
        print("choice1 wins")
    play_again = input("do u wish to continue(y/n): ")
    if play_again == "n":
        print("thank you")
        break
