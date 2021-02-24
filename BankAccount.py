import random

class BankAccount:
    routing_number = 123456789

    def __init__(self, full_name, account_number=None, balance = 0):
        if account_number is None:
                account_number = random.randint(10000000,99999999)
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        '''
        The deposit method will take one parameter amount and will add amount to the balance. 
        Also, it will print the message: “Amount Deposited: $X.XX”
        '''
        self.balance += amount
        print(f'Amount Deposited: ${amount:.2f}')

    def withdraw(self, amount):
        '''
        The withdraw method will take one parameter amount and will subtract amount from the balance. 
        Also, it will print a message, like “Amount Withdrawn: $X.XX”. 
        If the user tries to withdraw an amount that is greater than the current balance, 
        print ”Insufficient funds.” and charge them with an overdraft fee of $10
        '''
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
            print("$10.00 Overdraft fee applied")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount:.2f}")

    def get_balance(self):
        '''
        The get_balance method will print a user-friendly message with the account balance and then 
        also return the current balance of the account.
        '''
        print(f"Your current balance is ${self.balance:.2f}")
        return self.balance

    def add_interest(self):
        '''
        The add_interest method adds interest to the users balance. The annual interest rate is 1% (i.e. 0.083% per month). 
        Thus, the monthly interest is calculated by the following equation: interest = balance *  0.00083
        '''
        self.balance *= 1.00083

    def print_receipt(self):
        '''
        The print_receipt method prints a receipt with the account name, account number, and balance like this:
            Joi Anderson
            Account No.: ****5678
            Routing No.: 98765432
            Balance: $100.00
        '''
        print(self.full_name)
        print(f"Account No.: ****{str(self.account_number)[-4:]}")
        print(f"Routing No.: {BankAccount.routing_number}")
        print(f"Balance: ${self.balance:.2f}")

Luna = BankAccount("Luna Perry")

Luna.deposit(10000)

Luna.print_receipt()

