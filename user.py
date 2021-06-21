class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def make_deposit(self, amount):
        #making deposit
        self.balance += amount

    def make_withdrawal(self, amount):
        #have this method decrease the user's balance by the amount specified
        self.balance -= amount

    def display_user_balance(self):
        #have this method print the user's name and account balance to the terminal
        print(f"Hello mr. {self.name} You have ${self.balance} available ")