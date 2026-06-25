
def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Infinite"
    else:
        return a/b

num1=int(input("Enter the first number\n"))
operation=input("Enter the operation\n")
num2=int(input("Enter the second number\n"))

method_call={"+":sum,
             "-":subtract,
             "*":multiply,
             "/":divide}

print(method_call[operation](num1, num2))


