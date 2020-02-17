class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            amount -= 5
        return self
    def display_account_info(self):
        print("Balance: $", self.balance)
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        return (self.account.balance)
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        print(self.name, "-", self.account.balance)
        print(other_user.name, "-", other_user.account.balance)
        return self

sam = User("Sam Slag", "sam@sam.com")
judy = User("Judy Jetson", "jj@space.com")
tyler = User("Tyler Andy", "tyty@ty.net")

sam.make_deposit(111).make_deposit(111).make_deposit(111).make_withdrawal(3)
print(sam.account.balance)

judy.make_deposit(100).make_deposit(100).make_withdrawal(10).make_withdrawal(10)
print(judy.account.balance)

tyler.make_deposit(333).make_withdrawal(11).make_withdrawal(11).make_withdrawal(11)
print(tyler.account.balance)

sam.transfer_money(tyler, 69)


# sam2 = BankAccount(0.1, 1000)
# judy2 = BankAccount(0.01, 100)

# sam2.deposit(111).deposit(111).deposit(111).withdraw(333).yield_interest().display_account_info()
# judy2.deposit(100).deposit(100).withdraw(11).withdraw(11).withdraw(11).withdraw(11).yield_interest().display_account_info()