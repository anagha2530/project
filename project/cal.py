a = float(input("enter the no:"))
b = float(input("enter the no:"))

operator = ('+','-','*','/')

op = input("enter the operator:")
if op in operator:
    if op == '+':
        result = a + b
        print(result)
    elif op == '-':
        result = a - b
        print(result)
    elif op == '*':
        result = a * b
        print(result)
    elif op == '/':
        result = a / b
        print(result)
else:
    print("invalid")