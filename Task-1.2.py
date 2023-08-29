countodd = 0
counteven = 0
for i in range(1, 10):
    x = int(input("Enter a number:"))
    if x % 2 == 0:
        counteven += 1
    else:
        countodd += 1    
print("Count of even numbers",counteven)
print("Count of odd numbers ",countodd)




