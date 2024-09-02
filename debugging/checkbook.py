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
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

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
        # Prompt the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break  # Exit the loop and end the program
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()