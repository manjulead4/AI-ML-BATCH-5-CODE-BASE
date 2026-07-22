def discount(price,percentage):
    "calculate the discounted price "
    discounted_amount = price * (percentage/100)
    discounted_price = price - discounted_amount
    return discounted_price

item1 = discount(100,20)
item2 = discount(200,15)

print(item1,item2)