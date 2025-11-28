class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, acctName, initialAmount):
        self.name = acctName
        self.balance = initialAmount
        
        
    def check_acct(self):
        print(f""" 
            ******** Bank Of America ******
            
                Acct Name is: Mr.{self.name}
                Your Acct balance:$: {self.balance:.2f}\n
            
            ****** Thank You for Banking with Us *****
            """)
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"""Deposit is complete.""")
        self.check_acct()
    
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has balance of ${self.balance}:.2f"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.check_acct()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    def transfer(self, amount, account):
            try:
                print('\n*********\n\n Beginning Transfer...🚀🚀🚀🚀')
                self.viableTransaction(amount)
                self.withdraw(amount)
                account.deposit(amount)
                print('\nTransfer complete!😊\n\n********')
            except BalanceException as error:
                print(f'\nTransfer interrupted❌ {error}')
                
                
                
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.check_acct()
        
class SavingAcct(InterestRewardsAcct):
    def __init__(self, acctName, initialAmount):
        super().__init__(acctName, initialAmount)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.check_acct()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
        