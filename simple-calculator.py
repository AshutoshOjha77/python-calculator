a= int(input("Whats the first number? "))
b= int(input("whats the second number? "))
op= input("whats the operator? ")
if op=="+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b == 0:
        print("Error: Cannot divide by zero")
    else:    
        print(a/b)    
else:
    print("Error in operator")

