# conditional expression = A one-line shortcut for the if-else statement (ternary operator) 🐍
#                                             Print or assign one of two values based on a condition
#                                             X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

# logical operators = used on conditional statements 🐍

#              and = checks two or more conditions are True
#               or = checks if at least one condition is True
#              not = True if condition is False, and vice versa

temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is cloudy")
else:
    print("It is sunny")
    
#some string methods 🐍

name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

length = len(name)
index = name.find(" ")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count(" ")
phone_number = phone_number.replace("-", "")

# indexing = accessing elements of a sequence using [] (indexing operator) 🐍
#                     [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])

## format specifiers = {:flags} format a value based on what flags are inserted


price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f"price1 is: ${price1:}")
print(f"price2 is: ${price2:}")
print(f"price3 is: ${price3:}")