import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def display_result(die1, die2):
    print(f"You rolled {die1} and {die2} with a sum of {die1 + die2}")

def main():
    while True:
        print("VIRTUAL DIE ROLLER")
        roll = input("Press Enter to roll the dice or 'q' to quit: ")
        if roll.lower() == 'q':
            print("Exiting...")
            break
        die1, die2 = roll_dice()
        display_result(die1, die2)

if __name__ == '__main__':
    main()