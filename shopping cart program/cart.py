# a simple shopping cart program

shirts = []
prices = []
total = 0

while True:
    shirt = input("enter a brand to buy (e to exit): ")
    if shirt.lower() == "e":
        break
    else:
        price = float(input(f"enter the price of a {shirt}: $"))
        shirts.append(shirt)
        prices.append(price)

print("<<<<<< YOUR CART >>>>>>")
for shirt in shirts:
    print(shirt)
for price in prices:
    total += price
print()
print(f"the total cost of your items are: ${total}")
print("THANK YOU!")