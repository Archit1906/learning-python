# format specifiers = {value:flags} format a value based on what flags are inserted


# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 =3000.14159
price2 = -9807.65
price3 = 1200.34

print(f"Price 1: {price1:.2f}")  # Output: Price 1: 3000.14
print(f"Price 2: {price2:>10.2f}")  # Output: Price 2:   -9807.65
print(f"Price 3: {price3:<10.2f}")  # Output: Price 3: 1200.34   

print(f"price 1 is{price1:10}") # Output: price 1 is3000.14159
print(f"price 2 is{price2:10}") # Output: price 2 is  -9807.65
print(f"price 3 is{price3:10}") # Output: price 3 is   1200.34

print(f"price 1 is{price1:010.2f}") # Output: price 1 is0003000.14
print(f"price 2 is{price2:010.2f}") # Output: price 2 is-009807.65
print(f"price 3 is{price3:010.2f}") # Output: price 3 is0001200.34

print(f"price 1 is{price1:+.2f}") # Output: price 1 is+3000.14
print(f"price 2 is{price2:+.2f}") # Output: price 2 is-9807.65
print(f"price 3 is{price3:+.2f}") # Output: price 3 is+1200.34

print(f"price 1 is{price1:=+10.2f}") # Output: price 1 is+  3000.14
print(f"price 2 is{price2:=+10.2f}") # Output: price 2 is-  9807.65
print(f"price 3 is{price3:=+10.2f}") # Output: price 3 is+  1200.34

print(f"price 1 is{price1:^10.2f}") # Output: price 1 is 3000.14  
print(f"price 2 is{price2:^10.2f}") # Output: price 2 is -9807.65 
print(f"price 3 is{price3:^10.2f}") # Output: price 3 is  1200.34  

print(f"price 1 is{price1:,.2f}") # Output: price 1 is3,000.14
print(f"price 2 is{price2:,.2f}") # Output: price 2 is-9,807.65
print(f"price 3 is{price3:,.2f}") # Output: price 3 is1,200.34


