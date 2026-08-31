a = float(input("Enter value of a: "))
b = float(input("Enter Value of b: "))
operator = input("Enter Your operator:(+,-,*,/) ")

if operator == '+':
    print(a+b)
elif operator== '-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
else: 
    print("invalid calculation")    


