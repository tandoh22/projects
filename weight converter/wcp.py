# a simple weight converter program 
name = input('enter your name: ')
print(f"hello {name}, you are welcome!")
purpose = input('how may i assist you today? ')
print('okay, i got you!')
weight = float(input('how much do you weigh? '))
unit = input("in kilograms(Kg) or pounds(Lbs): ")

if unit == "kilograms":
    weight = weight * 2.205
    unit = 'Lbs'
elif unit == "pounds":
    weight = weight / 2.205
    unit = 'Kg' 
else:
    print(f"{unit} was invalid, try again") 

print(f"your weight in {unit} is {weight} {unit}")          