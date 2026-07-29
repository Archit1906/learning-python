# shopping cart program 

item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))   
total = price * quantity

print(total)
print(f"you have bought {quantity} x {item}/s")
print(f"your total is: ${total:.2f}")
