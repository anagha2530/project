inventory = {}
def add_item():
    item = input("enter the item to be added in dictionary: ")
    quantity = int(input("enter the quantity of " + item + ": "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(str (quantity) +  " of " + item + " has been successfully added")

def display_inventory():
    print("\n Current Inventory")
    for item,quantity in inventory.items():
        print(item + ":" + str(quantity))
    print()

def remove_item():
    item = input("enter the item to be removed: ")
    if item in inventory:
        del inventory[item]
        print(" " + item +" has been removed successfully: ")
    else:
        print(" "+ item +"not found")

def update_item():
    item = input("enter the item to be udated: ")
    if item in inventory:
        quantity = int(input("enter the new quantity of "+item+":"))
        inventory[item] = quantity
    else:
        print(" "+ item +" not found ")


def search_item():
    item = input("enter the item: ")
    if item in inventory:
        print(" "+ item + " has been found")
    else:
        print(" "+ item + " not found")

def main():
    while True:
        print("inventory tracker")
        print("""
              1.Add item
              2.remove item
              3.update item
              4.search item 
              5.display inventory
              6.exit""")
        ch = int(input("enter the choice(1,2,3,4,5,6): "))
        if ch == 1:
            add_item()
        elif ch ==2:
            remove_item()
        elif ch == 3:
            update_item()
        elif ch == 4:
            search_item()
        elif ch == 5:
            display_inventory()
        elif ch == 6:
            print("exit")
            break
        else:
            print("invalid choice")

if __name__ =="__main__":
    main()
