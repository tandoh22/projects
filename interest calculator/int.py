principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input('enter the principal amount: '))
    if principal <= 0:
        print('principal amount can not be less than or equal to zero')
while rate <= 0:
    rate = float(input('enter the rate: '))
    if rate <= 0:
        print('rate can not be less than or equal to zero')
while time <= 0:
    time = float(input('enter the time in years: '))
    if time <= 0:
        print('time can not be less than or equal to zero')
total_amount = principal * pow((1 + rate / 100), time)
print(f"your new total amount after {time} years/s is ${total_amount}")