"""Take the price of an item as input. If the price is more than 1000, apply a 10%
discount. Otherwise, check if the price is more than 500 and apply a 5% discount.
Print the final price."""

price=int(input("price k ho yesko ?"))
if price >= 1000:
    a = (price/100)*10
    print("the price is ",price-a)
elif price >= 500:
    a = (price/100)*5
    print("the price is ",price-a)
else:
    print("the price is ",price," no discount")