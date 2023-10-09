class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")

    @property
    def account_balance(self):
        return self.__account_balance


# Example usage:
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    my_account = BankAccount("123456789", "John Doe", 1000)

    # Deposit money
    my_account.deposit(500)

    # Withdraw money
    my_account.withdraw(200)

    # Display account balance
    my_account.display_balance()

    # Attempt to access account balance directly (this will work now)
    print(f"Account Balance: ${my_account.account_balance}")
