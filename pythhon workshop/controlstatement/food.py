# Dictionary containing 15 chicken dishes with their prices
menu = {
    "Chicken Biriyani": 200,
    "Chicken Fried Rice": 150,
    "Chicken Noodles": 140,
    "Chicken Pizza": 320,
    "Chicken Burger": 120,
    "Chicken Pasta": 180,
    "Chicken Manchurian": 160,
    "Chicken 65": 170,
    "Chicken Lolipop": 190,
    "Chicken Curry": 180,
    "Chicken Kebab": 200,
    "Chicken Tandoori": 250,
    "Chicken Shawarma": 100,
    "Chicken Soup": 90,
    "Chicken Sandwich": 110
}
dish = input("Enter the  dish name: ")
dish = dish.title()

if dish in menu:
    print(f"The price of {dish} is ₹{menu[dish]}")
else:
    print("Sorry, this dish is not available in the menu.")
