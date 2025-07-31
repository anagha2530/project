def add():
    id = input("enter the customer id : ")
    name = input("enter the customer name: ")
    address = input("enter the customer address")
    phone = input("enter the phone number: ")
    row = id + "\t" + name + "\t" + address + "\t" + phone + "\n"
    with open("customer.txt","a") as f:
         f.write(row)
         print("record added successfully")
         f.close()

def delete():
    id = input("enter the customer id to be deleted: ")
    with open("customer.txt","r") as f:
         all = f.readlines()
         f.close()
    with open("customer.txt","w") as f:
         flag = False
         for data in all:
              d = data.split("\t",1)
              if d[0] != id:
                   f.writelines(data)
              else:
                   flag = True
         f.close()
         if flag == True:
              print("Record deleted successfully")
         else:
              print("No record found")

def update():
    id = input("enter the customer id to be updated: ")
    with open("customer.txt","r") as f:
         all = f.readlines()
         f.close()
    with open("customer.txt","w") as f:
         flag = False
         for data in all:
              d = data.split("\t",1)
              if d[0] == id:
                    name = input("enter the new customer name: ")
                    address = input("enter the new customer address")
                    phone = input("enter the new phone number: ")
                    f.writelines(d[0] + "\t" + name + "\t" + address + "\t" + phone +"\n")
                    flag = True
              else:
                    f.writelines(data)
         f.close()

         if flag == True:
              print("record updated succesfully")
         else:
              print("record not found")

def search():
    id = input("enter the customer id to be searched: ")
    with open("customer.txt","r") as f:
         all = f.readlines()
         flag = False
         for data in all:
              d = data.split("\t",1)
              if d[0] == id:
                   print(data)
         if flag == False:
              print("No record found")
         f.close()

def show():
    f = open("customer.txt","r")
    print("id\tName\tAddress\tPhone")
    print(f.read())
    f.close()
print("CUSTOMER MANAGEMENT SYSTEM")
while True :
          print("""
          1.Add customer details: 
          2.Delete customer details: 
          3.Update customer details:
          4.Search for  customer: 
          5.Show all customers: 
          6.Exit""")
          ch = int(input("enter the choice(1,2,3,4,5,6): "))
          if ch == 1:
               add()
          elif ch == 2:
               delete()
          elif ch == 3:
               update()
          elif ch == 4:
               search()
          elif ch == 5:
               show()
          elif ch == 6:
               print("exit")
               break
          else:
               print("invalid choice")