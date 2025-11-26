

product_tuple = ("Laptop", "Mobile", "Tablet", "Keyboard", "Mouse",
                 "Charger", "Headset", "Monitor", "Printer", "Camera")

print("\nOriginal Tuple:", product_tuple)

print("First Item:", product_tuple[0])
print("Last Item:", product_tuple[-1])

print("First 3 Items:", product_tuple[:3])


print("Count of 'Laptop':", product_tuple.count("Laptop"))


print("Index of 'Printer':", product_tuple.index("Printer"))


print("Iterating Tuple:")
for p in product_tuple:
    print(p)
