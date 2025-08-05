def display_menu():
    print("VOTING SYSTEM MENU")
    print("""
          1. Vote
          2. View Result
          3. Exit""")
    
def vote(options):
    if not options:
        print("No options available.")
        return None
    
    print("VOTING OPTIONS")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    ch = input("Enter the option: ")
    if ch.isdigit() and 1 <= int(ch) <= len(options):
        return int(ch) - 1
    else:
        print("INVALID CHOICE")
        return None
        
def display_result(votes, options):
    """Display the vote count for each option."""
    print("Counting votes")
    print("Voting results")
    for i, count in enumerate(votes):
        print(f"{options[i]}: {count} votes")

def main():
    options = ("OPTION 1", "OPTION 2", "OPTION 3")
    votes = [0] * len(options)

    while True:
        display_menu()
        try:
            ch = input("Enter the option (1,2,3): ").strip()
            if ch.isdigit():
                ch = int(ch)
            else:
                print("INVALID CHOICE: Please enter a number.")
                continue

            if ch == 1:
                vote_choice = vote(options)
                if vote_choice is not None:
                    votes[vote_choice] += 1
                    print("Your vote has been recorded")
            elif ch == 2:
                display_result(votes, options)
            elif ch == 3:
                print("Exiting voting system...")
                break
            else:
                print("INVALID CHOICE: Please choose 1, 2, or 3.")
        except ValueError:
            print("INVALID CHOICE: Please enter a valid number.")

if __name__ == "__main__":
    main()