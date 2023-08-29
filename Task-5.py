num1=float(input("Enter the 1 st number: "))
num2=float(input("Enter the 2 nd number: "))
operator=str(input("Enter the operator: "))
if operator=='*':
    value=num1*num2
elif operator=='-':
    value=num1-num2
elif operator=='+':
    value=num1+num2
elif operator=='/':
    value=num1/num2
else:
    print("The operator is invalid")
print(f"Result:{value}")

