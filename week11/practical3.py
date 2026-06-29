# --------------------------------------------------
# Restaurant Ordering System

# This program allows customers to place food orders
# from a menu. Users can:
# 1. Add food items to their order
# 2. View a summary of all orders
# 3. Calculate the total cost
# 4. Exit the program
# --------------------------------------------------

# Store the menu items and their prices
prices = {
    'chicken': 8.50,
    'steak': 13.80,
    'fish': 9.80,
    'pasta': 9.50,
    'coffee': 2.50,
    'tea': 1.80,
    'water': 0.50
}

# Store the customer's orders
# Format: {item: quantity}
orders = {}

# Keep showing the menu until the user chooses to quit
while True:

    # Display the main menu
    print("""
--------------------
1. Add order
2. Summarize orders
3. Quit
--------------------
""")

    # Ask the user to choose an option
    choice = int(input("Your choice? "))

    # Option 1: Add a new order
    if choice == 1:

        # Display the food menu and prices
        print(f'{"Item":<10}{"Price":<10}')
        print(f'{"----":<10}{"-----":<10}')

        for item, price in prices.items():
            print(f'{item.title():<10}${price:.2f}')

        # Ask the user which item they want to order
        order = input("Your order? ").lower()

        # Check whether the item is on the menu
        if order in prices:

            # Ask how many sets the user wants
            sets = int(input("How many sets? "))

            # If this is the first time ordering the item,
            # save it in the dictionary
            if order not in orders:
                orders[order] = sets

            # Otherwise, add the new quantity to the existing order
            else:
                orders[order] += sets

            print(f'{sets} sets of {order} ordered.')

            # Example output:
            # 2 sets of chicken ordered.

        # Display a message if the item is not available
        else:
            print(f'{order} is not available.')

            # Example output:
            # burger is not available.

    # Option 2: Display the order summary
    elif choice == 2:

        print(f'{"Item":<10}{"Quantity":<10}')
        print(f'{"----":<10}{"--------":<10}')

        # Store the total cost of all orders
        total_cost = 0

        # Display each ordered item and quantity
        for order, sets in orders.items():
            print(f'{order.title():<10}{sets:<10}')

            # Calculate the total cost
            total_cost += prices[order] * sets

        print(f'\nTotal cost = ${total_cost:.2f}')

        # Example output:
        #
        # Item      Quantity
        # ----      --------
        # Chicken   2
        # Coffee    1
        #
        # Total cost = $19.50

    # Option 3: Exit the program
    elif choice == 3:
        break

    # Display an error message if the menu option is not valid
    else:
        print("Invalid choice.")

        # Example output:
        # Invalid choice.
