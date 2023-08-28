temp=int(input("Enter the temparature: "))
unit=str(input("Enter c for celsius or f for fahrenheit: "))
if unit=="c"or unit=='C':
    print("Value is in celsius and we need to convert it to Fahrenheit")
    Fahrenheit=(temp*9/5)+32
    print(f"Fahrenheit value after conversion from celsius is {Fahrenheit} F")
elif unit=="f" or unit=='F':
    print("Value is in Fahrenheit so we need to convert it to celsius")
    Celsius=(temp-32)*5/9
    print(f"Celsius value after conversion from Fahrenhiet is {Celsius} c")