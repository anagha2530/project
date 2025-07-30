to_do_list = []
completed_list = []

def add_items():
    items = input("enter the items to be added in the list: ")
    to_do_list.append(items)
    print(" " + items + " has been added")

def remove_items():
    index = input("enter the item to be removed: ")
    if index.isdigit() and 1 <= int(index) <= len(to_do_list):
        removed_item = to_do_list.pop(int(index)-1)
        print(" " + removed_item + "has been succesfully removed")
    else:
        print("invalid index")

def display_list(lst,lst_name):
    print("\n" + lst_name + ":")
    for index,items in enumerate(lst,start=1):
        print(str(index) + "." + items)
    print()

def mark_item_completed():
    index = input("enter the index to be marked completed: ")
    if index.isdigit() and 1 <= int(index) <= len(to_do_list):
        completed_item = to_do_list.pop(int(index)-1)
        completed_list.append(completed_item)
        print(" "+ completed_item + " has been marked as completed")
    else:
        print("invalid index")

def main():
    while True:
        print("TO_DO_LIST")
        print("""
            1.ADD TO LIST
            2.REMOVE FROM LIST
            3.MARK ITEM AS COMPLETED
            4.COMPLETED LIST
            5.DISPLAY LIST
            6.EXIT""")
        ch = int(input("enter the choice(1,2,3,4,5,6): "))
        if ch == 1:
            add_items()
        elif ch == 2:
            remove_items()
        elif ch == 3:
            mark_item_completed()
        elif ch == 4:
            display_list(to_do_list,"TO_DO_LIST")
        elif ch == 5:
            display_list(completed_list,"COMPLETED LIST")
        elif ch == 6:
            print("exit")
            break
        else:
            print("invalid choice")

if __name__ == '__main__':
    main()