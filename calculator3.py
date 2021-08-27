operation = "module"
a = int(input("enter number a : "))
b = int(input("enter number b : "))
if operation == "add":
    c = a+b
    print("addition is = {}".format(c))
elif operation == "sub":
    c = a-b
    print("subtraction is = {}".format(c))
elif operation == "multiply":
    c = a*b
    print("multiply is = {}".format(c))
elif operation == "divide":
    c = a/b
    print("divide is = {}".format(c))
elif operation == "module":
    c = a%b
    print("module is = {}".format(c))
else:
    print("wrong")