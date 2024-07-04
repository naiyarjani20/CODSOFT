#Calculator program by python by adding arithematic operations
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choose = int(input("Enter (1/2/3/4)"))
x=int(input("Enter a number"))
y=int(input("Enter another number"))
if choose== 1:
    print(x, "+", y,"=",add(x,y))
elif choose==2:
    print(x, "-" ,y,"=",subtract(x,y))
elif choose==3:
    print(x, "*" ,y,"=",multiply(x,y))
elif choose==4:
    print(x, "/", y,"=",divide(x,y))
else:
    print("Invalid input")
