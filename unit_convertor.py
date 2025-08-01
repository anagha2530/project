def inches_to_cm(inches):
    return inches * 2.54
def cm_to_inches(cm):
    return cm / 2.54
def kg_to_pounds(kg):
    return kg/0.453592
def pounds_to_kg(pounds):
    return pounds * 0.453592
def fah_to_cel(fah):
    return (fah-32) * 5.0/9.0
def cel_to_fah(cel):
    return (cel * 9.0/5.0) + 32

def unit_converter():
    print("UNIT CONVERTOR")
    print("""
          1.Length
          2.Weight
          3.Temperature""")
    ch = int(input("enter the choice(1,2,3):"))
    if ch == 1:
        print("Length conversions: ")
        print("a.Inches to Centimeter")
        print("b.Centimeter to Inches")
        sub_choice = input("enter the choice(a,b): ")
        if sub_choice == 'a':
            inches = float(input("enter the inches: "))
            print(inches,"inches is",inches_to_cm(inches),"cm")
        elif sub_choice == 'b':
            cm = float(input("enter the cm: "))
            print(cm,"cm is",cm_to_inches(cm),"inches")
        else:
            print("INVALID CHOICE")

    elif ch == 2:
        print("Weight conversions: ")
        print("a.kg to pounds")
        print("b.pounds to kg")
        sub_choice = input("enter the choice(a,b): ")
        if sub_choice == 'a':
            kg = float(input("enter the kg: "))
            print(kg,"kg is",kg_to_pounds(kg),"pounds")
        elif sub_choice == 'b':
            pounds = float(input("enter the pounds: "))
            print(pounds,"pounds is",pounds_to_kg(pounds),"kg")
        else:
            print("INVALID CHOICE")

    elif ch == 3:
        print("Temperature conversions: ")
        print("a.Fah to cel")
        print("b.Cel to Fah")
        sub_choice = input("enter the choice(a,b): ")
        if sub_choice == 'a':
            fah = float(input("enter the fah: "))
            print(fah,"fah is",fah_to_cel(fah),"cel")
        elif sub_choice == 'b':
            cel = float(input("enter the cel: "))
            print(cel,"cel is",cel_to_fah(cel),"fah")
        else:
            print("INVALID CHOICE")

    else:
        print("Invalid choice")


unit_converter()
    

