def add_expense(expenses):
    # Loop to ensure valid input
    while True:
        try:
            amount = float(input("Enter your expense amount: "))
            if amount <= 0:
                print("You must enter a positive value.")
                continue
        except ValueError:
            print("Invalid Input! Please enter a number.")
            continue
        break

    # Categories available
    categories = ["food", "transport", "entertainment", "others"]

    # Loop to ensure valid category input
    while True:
        category = input("Which category do you want? (Food, Transport, Entertainment, Others): ").lower()
        if category not in categories:
            print("Invalid Input! Please enter a valid category.")
        else:
            break

    description = input("Enter your description (Optional): ")

    # Adding expense to the list
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    print("Expense added successfully!\n")


def display_summary(expenses):
    summary = {}

    # Summarizing expenses by category
    for expense in expenses:
        if expense["category"] in summary:
            summary[expense["category"]] += expense["amount"]
        else:
            summary[expense["category"]] = expense["amount"]

    # Displaying the summary
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category.capitalize()}: ${total:.2f}")
    print()


def main():
    expenses = []

    while True:
        print("Choose an option:")
        print("1. Add an expense")
        print("2. View expense summary")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
