class BankAccount:
    routing_number = 123456789

    def __init__(self, full_name, account_number, balance = 0):
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


Luna = BankAccount("Luna Perry", 12345678)

Luna.deposit(5000)
print(Luna.__dict__)
Luna.withdraw(1000)
print(Luna.__dict__)

Luna.get_balance()

Luna.add_interest()
Luna.get_balance()