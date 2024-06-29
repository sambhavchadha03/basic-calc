

num1 =float(input("ENTER THE 1ST NUMBER: "))
num2= float(input("ENTER THE 2ND NUMBER:  "))
operator=input("ENTER AN OPERATOR(+ - * /): ")
if operator == "+":
    result=num1+num2
    print(result)

elif operator =="-":
    result=num1-num2
    print(result)

elif operator =="%":
    result=num1%num2
    print(result)

elif operator =="/":
    result=num1/num2
    print(result)

else:
    print(f"{operator}THIS IS NOT A VALID OPERATOR")




