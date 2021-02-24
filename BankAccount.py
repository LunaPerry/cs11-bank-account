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

Luna = BankAccount("Luna Perry", 12345678)

Luna.deposit(5)
print(Luna.__dict__)