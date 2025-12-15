print("WELCOME TO ARNAV'S GROCERY ITEM APP")
print("🥦---🧺----🍅----💊----🥩----🧀-")
print("\n")
foods = []
prices = []
total = 0

# Tax rate input with validation
while True:
    try:
        tax_rate = float(input("Enter tax rate (e.g. 10 for 10%): "))
        if tax_rate >= 0:
            break
        print("Tax rate must be 0 or positive!")
    except ValueError:
        print("Enter a valid number!")

while True:
    print("\n🛒 Grocery Cart")
    print("1) Add item 🛒")
    print("2) Show cart & Exit")
    
    # Menu validation
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in (1, 2):
                break
            print("Enter 1 or 2 only!")
        except ValueError:
            print("Enter a number!")

    if choice == 2:
        break
    
    # Item input
    item = input("Enter a Grocery Item (q to quit): ").strip()
    if item.lower() == 'q':
        break
        
    # Price validation
    while True:
        try:
            price = float(input(f"💵 Enter price for {item}: $"))
            if price >= 0:
                break
            print("Price must be 0 or positive!")
        except ValueError:
            print("Enter a valid price!")

    foods.append(item)
    prices.append(price)
    print(f"✅ Added {item} for ${price}")

# Final cart display
print("\n" + "="*30)
print("        CART TOTAL")
print("="*30)
for item, price in zip(foods, prices):
    print(f"{item}: ${price:.2f}")

total = sum(prices)
tax_amount = total * (tax_rate / 100)
grand_total = total + tax_amount

print(f"\nSubtotal:     ${total:.2f}")
print(f"Tax ({tax_rate}%): ${tax_amount:.2f}")
print(f"Grand Total:  ${grand_total:.2f}")
print("="*30)

input("\nPress ENTER to exit...")
