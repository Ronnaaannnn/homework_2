price = float(input("Enter the price of the item: "))

if price > 1000:
    new_price = price - (price * 0.20)
    print("New price after 20% discount:", new_price)
elif 500 <= price <= 1000:
    new_price = price - (price * 0.10)
    print("New price after 10% discount:", new_price)
else:
    print("No discount. Price:", price)
