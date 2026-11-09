
# Function to calculate the budget
def calculate_budget(income, expenses):
    return income - expenses


# Loop to run the budget tracker
while True:

    # Ask the user for their income and expenses
    income = float(input("Enter your income: $"))
    expenses = float(input("Enter your total expenses: $"))

    # Call the function to calculate the balance
    balance = calculate_budget(income, expenses)

    # Display the budget information
    print("\n--- Budget Tracker ---")
    print("Income: $", income)
    print("Expenses: $", expenses)
    print("Money left: $", balance)

    # If statement to check the remaining balance
    if balance < 0:
        print("You spent more than your income.")
    elif balance == 0:
        print("You used all your income.")
    else:
        print("You have money left to save!")

    # Ask the user if they want to continue
    again = input("\nCalculate another budget? (yes/no): ")

    # Stop the loop if the user enters no
    if again.lower() == "no":
        print("Thank you for using Budget Tracker!")
        break
