#welcome message
print("hello! all you have to do is write things you want to buy and also price and then we will calculate how much it will cost all together!;D")

#user has to write items/things
items = []
total_cost = 0

while True:
    #if user is done writing then he/she has to write "done"
    item = input("Enter item (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input("Enter price: "))
    items.append((item, price))
    total_cost += price

print("\nItems Purchased:")
for item, price in items:
    print(f"{item}: ${price:.2f}")

#calculating total price of all items
print(f"\nTotal Cost: ${total_cost:.2f}")