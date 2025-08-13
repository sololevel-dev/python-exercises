#python calculator

operator=input('Enter an operator (+ - * /): ')
num1=float(input('Enter first num: '))
num2=float(input('Enter second num: '))

if operator=='+':
    result=num1+num2
    print(round(result,3))
elif operator=='-':
    result=num1-num2
    print(round(result,3)) 
elif operator=='/':
    result=num1/num2
    print(round(result,3))
elif operator=='*':
    result=num1*num2
    print(round(result,3))
else:
    print(f'{operator} is not valid operator')               