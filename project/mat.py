import numpy as np

def matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    mat = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Element at ({i + 1}, {j + 1}): ")) 
            row.append(element)
        mat.append(row)
    return np.array(mat)

def matrix_operation():
    print("MATRIX CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter the operation number (1-4): "))

    print("Enter Matrix 1:")
    matrix1 = matrix()
    print("Enter Matrix 2:")
    matrix2 = matrix()

    res = None  # <-- define res with default

    try:
        if choice == 1:
            res = np.add(matrix1, matrix2)
        elif choice == 2:
            res = np.subtract(matrix1, matrix2)
        elif choice == 3:
            res = np.matmul(matrix1, matrix2)
        elif choice == 4:
            res = np.divide(matrix1, matrix2)
        else:
            print("Invalid choice.")
            return  # exit early if invalid

        print("Result:\n", res)

    except ValueError as e:
        print("Matrix shape mismatch:", e)

matrix_operation()
