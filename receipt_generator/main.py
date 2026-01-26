print("===== RECEIPT GENERATOR =====")

items = []
total = 0

while True:
    name = input("Enter item name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter price of item: "))
    quantity = int(input("Enter quantity: "))

    cost = price * quantity
    total += cost

    items.append((name, price, quantity, cost))

print("\n===== RECEIPT =====")
print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Price", "Qty", "Cost"))

for item in items:
    print("{:<15} {:<10} {:<10} {:<10}".format(item[0], item[1], item[2], item[3]))

print("-------------------------------")
print(f"Total Amount: ₹{total}")
print("Thank you for shopping! 😊")
