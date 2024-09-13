def calculate_tip(total_amount, tip_percentage):
    """Calculate the tip based on the total amount and tip percentage."""
    tip_amount = total_amount * (tip_percentage / 100)
    total_with_tip = total_amount + tip_amount
    return tip_amount, total_with_tip


def tip_calculator():
    """Run the tip calculator."""
    print("Welcome to the Tip Calculator!")

    # Get the user input for the total bill amount
    while True:
        try:
            total_amount = float(input("Enter the total bill amount: "))
            if total_amount <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a positive number.")

    # Get the user input for the tip percentage
    while True:
        try:
            tip_percentage = float(input("Enter the tip percentage (e.g., 25 for 25%): "))
            if tip_percentage < 0:
                print("Please enter a tip greater than or equal to 0.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a positive tip.")

    # Determine if they are splitting
    while True:
        try:
            split_amount = int(input("Enter the amount of people to split with: "))
            if split_amount in range(0, 2):
                print("You are either generous or have no friends!")
                break
            elif split_amount > 1:
                print(f"You are splitting with {split_amount} people.")
                break
        except ValueError:
            print("Invalid input, please enter 0 or larger.")

    # Calculate the tip and total amount
    tip_amount, total_with_tip = calculate_tip(total_amount, tip_percentage)

    # Display results
    if split_amount in range(0, 2):
        print(f"Tip amount = ${tip_amount:.2f}")
        print(f"Total amount (including tip): ${total_with_tip:.2f}")
    else:
        individual_amount = float(total_with_tip / split_amount)
        print(f"Tip amount = ${tip_amount:.2f}")
        print(f"Total amount (including tip): ${total_with_tip:.2f}")
        print(f"Each person pays ${individual_amount:.2f}")


# Run the tip calculator
tip_calculator()
