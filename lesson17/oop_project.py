from bank_accounts import *


Dumindu = BankAccount("A.Dumindu Viraj",10000000000)
Shakthi = BankAccount("A.Shakthi Danisha",99000000000)
Dumindu.deposit(59440000)
Dumindu.withdraw(678800)
Dumindu.check_acct()
Dumindu.transfer(7779, Shakthi)

JointAcc = InterestRewardsAcct("DVS", 1000)
JointAcc.check_acct()
JointAcc.deposit(100)
JointAcc.transfer(100, Dumindu)

Viraj = SavingAcct("Viraj", 50000000)
Viraj.check_acct()
Viraj.deposit(450000)
Viraj.transfer(1000, Shakthi)