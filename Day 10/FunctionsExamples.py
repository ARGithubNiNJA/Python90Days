
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

def calculator():
    should_continue=True
    num1=float(input("Enter the first number\n"))
    while should_continue:
        operation=input("Enter the operation\n")
        num2=float(input("Enter the next number\n"))

        method_call={"+":sum,
                     "-":subtract,
                     "*":multiply,
                     "/":divide}
        result=method_call[operation](num1,num2)
        print(f"{num1}{operation}{num2}={result}")
        ask=input("Do you want to continue?(y/n)\n")
        if ask.lower()=="y":
            num1=result
        else:
            should_continue=False
            print("\n"*20)
calculator()  ##recurssion



