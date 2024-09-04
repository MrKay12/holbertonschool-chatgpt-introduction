#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook class that allows for depositing, withdrawing, and checking balance.
    """

    def __init__(self):
        """
        Initializes the checkbook with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook balance.

        Parameters:
        amount (float): The amount of money to deposit. Must be a positive number.

        Returns:
        None
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw. Must be a positive number.

        Returns:
        None
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Error: Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Returns:
        None
        """
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    """
    The main function that provides an interactive console for the user to manage their checkbook.

    The user can:
    - Deposit money
    - Withdraw money
    - Check the balance
    - Exit the program

    Returns:
    None
    """
    cb = Checkbook()  # Create an instance of Checkbook
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break  # Exit the loop and end the program

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid number for the deposit amount.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid number for the withdrawal amount.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()