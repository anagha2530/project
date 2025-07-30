import numpy as np

def matrix():
    rows = int(input("enter the number of rows: "))
    cols = int(input("enter the number of coloumns: "))
    mat = []
    print("enter the elements row wise: ")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"the elements are {[i +1],[j + 1]}: ")) 
            row.append(element)
        mat.append(row)
    return np.array(mat)

def matrix_operation():
    print("MATRIX CALCULATOR")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")

    choice = int(input("enter the operation: "))
    matrix1 = matrix()
    matrix2 = matrix()

    if choice == 1:
        res = np.add(matrix1,matrix2)
    elif choice == 2:
        res = np.subtract(matrix1,matrix2)
    elif choice == 3:
        res = np.matmul(matrix1,matrix2)
    elif choice == 4:
        res = np.divide(matrix1,matrix2)
    else:
        print("invalid choice") 
    print(res)
    return

matrix_operation()
