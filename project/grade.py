students = {}

while True:
    print("student grade card")
    print("1.add the student name and grade")
    print("2.update the student grade")
    print("3.show all the student grade")
    print("4.average of total grade")
    print("5.exit\n")

    choice = int(input("enter the choice(1-5): "))
    if choice == 1:
        name = input("enter the students name: ")
        grade = float(input("enter the student grade: "))
        students[name] = grade
        print("student added successfully")

    elif choice == 2:
        name = input("enter the name: ")
        if name in students:
            new_grade = float(input("enter the student's new_grade: "))
            students[name] = new_grade
            print("student updated successfully")
        else:
            print("student not found")

    elif choice == 3:
        if students:
            print("Students : Grade")
            for i in students:
                print(i , ":",students[i])
        else:
            print("dictionary is empty")
    
    elif choice == 4:
        if students:
            total_grade = sum(students.values())
            average_grade = total_grade/len(students)
            print("average of class is : ",average_grade)
        else:
            print("dictionary is empty")

    elif choice == 5:
        break

    else:
        print("invalid choice")
