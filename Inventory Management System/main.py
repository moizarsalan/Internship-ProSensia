# Initialize the inventory as an empty list
inventory = []

# Function to add new products to the inventory
def add_prod():
    prod_name = input("Enter product name: ")
    prod_id = input("Enter product ID: ")
    quantity = input("Enter product quantity: ")
    price = input("Enter product price: ")

    # Create a dictionary for the product
    product = {
        'name': prod_name,
        'id': prod_id,
        'quantity': quantity,
        'price': price
    }

    # Add the product to the inventory
    inventory.append(product)
    print(f"Product '{prod_name}' added successfully!\n")

# Function to view the current inventory
def view_inven():
    if not inventory:
        print("No products in the inventory!\n")
        return

    print("Current Inventory:")
    for product in inventory:
        print(f"Name: {product['name']}, ID: {product['id']}, Quantity: {product['quantity']}, Price: {product['price']}")
    print()

# Function to update the quantity of an existing product
def up_prod_quantity():
    prod_id = input("Enter product ID to update: ")

    # Find the product by ID
    for product in inventory:
        if product['id'] == prod_id:
            new_quantity = int(input(f"Enter new quantity for product '{product['name']}': "))
            product['quantity'] = new_quantity
            print(f"Quantity for product '{product['name']}' updated successfully!\n")
            return

    print(f"Product with ID '{prod_id}' does not exist!\n")

# Function to remove a product from the inventory
def remove_prod():
    prod_id = input("Enter product ID to remove: ")

    # Find the product by ID and remove it
    for product in inventory:
        if product['id'] == prod_id:
            inventory.remove(product)
            print(f"Product '{product['name']}' removed successfully!\n")
            return

    print(f"Product with ID '{prod_id}' does not exist!\n")

# Main function to drive the program
def main():
    while True:
        print("Welcome to Inventory Management System!\nDeveloped by Abdul Moiz Arsalan")
        print("1. Add a New Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove a Product")
        print("5. Exit")

        choose = input("Choose an option: ")

        if choose == '1':
            add_prod()
        elif choose == '2':
            view_inven()
        elif choose == '3':
            up_prod_quantity()
        elif choose == '4':
            remove_prod()
        elif choose == '5':
            print("Thank you for using the Inventory Management System!")
            break
        else:
            print("Invalid choice, please try again!\n")

# Run the main function
if __name__ == '__main__':
    main()