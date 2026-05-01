class BankAccount:
    def __init__(self,balance):
        self.__balanace=balance

    def deposit(self,amount):
        self.__balanace+=amount

    def get_balance(self):
        return self.__balanace





acc=BankAccount(1000)
acc.deposit(500)
print(acc.get_balance()) 
