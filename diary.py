import os
from datetime import datetime

def write_entry():
    entry = input("enter the diary sentence: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt","a") as file:
        file.write(f"{timestamp}\n{entry}\n\n")

def view_entries():
    if not os.path.exists("diary.txt"):
        print("no diary entries found")
        return
    with open("diary.txt","r") as file:
        entries = file.read()
        print("\n diary entries")
        print(entries)

def main():
    while True:
        print("PERSONAL DIARY")
        print("""
            1.Write a new entry
            2.view past entries
            3.exit""")
        ch = int(input("enter the choic(1,2,3): "))
        if ch == 1:
            write_entry()
        elif ch == 2:
            view_entries()
        elif ch == 3:
            print("exit")
            break
        else:
            print("Invalid choce")

if __name__ == "__main__":
    main()
