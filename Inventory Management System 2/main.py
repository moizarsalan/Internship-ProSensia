# Inventory Management System
# Developed by Abdul Moiz Arsalan

# Function to add new products
def add_prod(inventory):
    name = input("Enter Product Name: ").strip()
    if name in [product['name'] for product in inventory]:
        print("Product already exists in inventory!")
    else:
        try:
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            inventory.append({'name': name, 'price': price, 'quantity': quantity})
            print(f"Product {name} added to inventory!")
        except ValueError:
            print("Invalid Input! Price should be a number and quantity should be an integer.")

# Function to update the quantity of an existing product
def up_Quantity(inventory):
    name = input("Enter Product Name: ").strip()
    for product in inventory:
        if product['name'].lower() == name.lower():
            try:
                new_quantity = int(input("Enter New Quantity: "))
                product['quantity'] = new_quantity
                print(f"Quantity for {name} updated successfully!")
                return
            except ValueError:
                print("Invalid Input! Quantity should be an integer.")
                return
    print("Product not found!")

# Function to display all products in inventory
def display_inventory(inventory):
    if not inventory:
        print("No products in the inventory.")
    else:
        print("\nCurrent Inventory:")
        print(f"{'Name':<20}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        for product in inventory:
            print(f"{product['name']:<20}{product['price']:<10}{product['quantity']:<10}")
        print("-" * 40)

# Main function to manage the inventory system workflow
def main():
    inventory = []
    while True:
        print("\nWelcome to Inventory Management System!")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_prod(inventory)
        elif choice == '2':
            up_Quantity(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            print("Thank you for using the Inventory Management System!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
