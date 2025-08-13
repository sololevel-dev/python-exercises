
weight=float(input('Enter your weight: '))
unit=input('Kilograms or Pounds? (K or L): ')

if unit.lower()=='k':
    weight=weight * 2.205
    unit='LBS.'
elif unit.lower()=='l':
   weight=weight / 2.205
   unit='Kgs.'
else:
    print(f'{unit} was not valid') 
 
print(f'your weight is: {round(weight,1)} {unit} ')           