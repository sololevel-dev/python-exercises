foods=[]
prices=[]
total=0
while True:
    food=input('Enter your food like to eat!: ')
    if food.lower()=='q':
        break
    else:
        price=float(input('Enter the price of food $:'))
        prices.append(price)
        foods.append(food)
        
        
print('----------your payment-----------')
for food in foods:
    print(food,end=' ')
    
for price in prices:
    total+=price

print()
print(f"your total payment is {total:2} for {len(foods)} foods")