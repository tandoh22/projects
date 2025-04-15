# a simple shopping cart program

shirts = []
prices = []
total = 0

while True:
    shirt = input("enter a brand to buy: ")
    if shirt.lower() == "e":
        break
    else:
        price = float(input("enter the price of a {shirt}: $"))
        shirts.append(shirt)
        prices.append(price)
print("<<<<<< YOUR CART >>>>>>")