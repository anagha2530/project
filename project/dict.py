my_dict = {}
while True:
    print("english dictionary")
    print("\n1.enter the word and definition \n 2.find the definition \n 3.exit""")
    choice = int(input("enter the no(1-3): "))
    if choice == 1:
        word = input("enter the word: ")
        defi = input("enter the definition")
        my_dict[word]=defi
        print(word,"is added to dict")
    elif choice == 2:
        word = input("enter the word: ")
        if word in my_dict:
            print("the definition of word is : ",defi)
        else:
            print("word not found")
    elif choice == 3:
        break
    else:
        print("invalid")