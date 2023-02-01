class Account():

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def __str__(self):
    return f"{self.owner}'s account has a current balance is {self.balance}"

  def __len__(self):
    return self.balance

  def deposit(self,balance):
    self.balance += balance
    print(f'Deposit Accepted, your new balance is {self.balance}')

  def withdraw(self, balance):
    if balance > self.balance:
      print("Insufficient funds..")
      return 

    self.balance -= balance
    print(f'Withdrawal completed, your new balance is {self.balance}')

gary = Account("Gary", 500)
print(gary)
gary.deposit(500)
gary.deposit(1)
gary.deposit(200)

gary.withdraw(200)

gary.withdraw(1202)