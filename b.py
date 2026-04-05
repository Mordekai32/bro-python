num1=int(input("Enter first number:"))
op=input("Enter operator:")
num2=int(input("Enetr second number"))
if op=="+":
    print (num1+num2)
elif op=="-":
    print (num1-num2)
elif op=="*":
    print (num1*num2)
elif op=="/":
    if num1/num2%0:
        print (num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
 print("Error: Invalid operator.")