class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        if balance<0:
            raise ValueError("Balance amount must be positive!")
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount should not be negative!")
        if amount > self.balance:
            raise ValueError("Not enough balance!")

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should not be negative!")

        self.balance += amount
        return self.balance

class SavingsAccount(Account):
    def __init__(self, owner, interest_rate, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate
    @interest_rate.setter
    def interest_rate(self, interest_rate):
        if interest_rate<=0:
            raise ValueError("Interest rate must be positive!")
        elif not 0<interest_rate<=1:
            raise ValueError("Interest rate should be beetween 0 to 1!")
        self._interest_rate = interest_rate
        
    def add_interest_rate(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def get_account(self, account_id=None):
        account = self.accounts.get(account_id)

        if account is None:
            raise ValueError("This account id does not exists!")
        return account

    def add_account(self, account, account_id=""):
        if account_id == "":
            while True:
                account_id = f"{self.next_account_number:06d}"
                self.next_account_number += 1
                if self.accounts.get(account_id) is None:
                    break
        if not account_id.isdigit() or len(account_id) != 6:
            raise ValueError("Acount id is not correct!")
        if account_id in self.accounts:
            raise ValueError("This account Id already exists!")
        self.accounts[account_id] = account

    def transfer(self, from_id, to_id, amount):
        account1 = self.get_account(from_id)
        account2 = self.get_account(to_id)
        account1.withdraw(amount)
        account2.deposit(amount)