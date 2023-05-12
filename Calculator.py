def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
print("Select your choice")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\n5.Exit")
oper = int(input("Choose the option to perform the operation: "))
while True:
    if oper in (1,2,3,4,5):
        if oper == 1:
            print("Addition result: ", add(num1,num2))
        elif oper == 2:
            print("Subtraction result: ", sub(num1,num2))
        elif oper == 3:
            print("Multiplication result: ", mul(num1,num2))
        elif oper == 4:
            print("Division result: ", div(num1,num2))
        else:
            break
    else:
        print("Provide Valid Option")