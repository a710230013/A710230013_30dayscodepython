class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Jumlah deposit harus lebih dari nol!")
            self.balance += amount
            print(f"Deposit sebesar {amount} berhasil dilakukan. Saldo sekarang: {self.balance}")
        except ValueError as e:
            print(e)
     
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Saldo tidak mencukupi untuk melakukan penarikan!")
            self.balance -= amount
            print(f"Penarikan sebesar {amount} berhasil dilakukan.Saldo sekarang: {self.balance}")
        except ValueError as e:
            print(e)

my_account = BankAccount(1000)

my_account.deposit(-500)

my_account.deposit(500)

my_account.withdraw(1500)

my_account.withdraw(500)