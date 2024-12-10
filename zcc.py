class Account:
    def __init__(self,Bal,Acc_no):
        self.Balance=Bal
        self.Account_number=Acc_no
        print('\nAcount number',self.Account_number,'is unlocked with the balance of',self.Balance,'/-.')
        print('\n(PIN is the reversal of the Account number)')
    def credit(self, cred, pin):
        if pin==int(str(acc_no)[::-1]):
               self.Balance += cred
               print('\nRs',cred,"/-was credited to Acc no:",acc1.Account_number)
               print('\nRs',self.bal(),'/-is your total balance')
               print('\nThank you for using the service... \nAccount LOCKED.')
        else:
              print('\nINCORRECT PIN..AMOUNT NOT CREDITED..ACCOUNT LOCKED!')                
    def debit(self, deb, pin):
        if pin==int(str(acc_no)[::-1]):
             self.Balance -= deb
             print('\nRs',deb,"/- was debited from Acc no:",acc1.Account_number)
             print('\nRs',self.bal(),'/- is your total balance')
             print('\nThank you for using the service... \nAccount LOCKED.')
        else:
             print('\nINCORRECT PIN..AMOUNT NOT DEBITED..ACCOUNT LOCKED!')  
    def bal_enq(self, pin):
      if pin==int(str(acc_no)[::-1]):
            print('\nRs',acc1.bal(),'/-is your total balance')
            print('\nThank you for using the service... \nAccount LOCKED.')
      else:
            print('\nINCORRECT PIN..BALANCE CANT BE CHECKED..ACCOUNT LOCKED!')
    def bal(self):
          return self.Balance      
acc_no=input('Set the A/c no(use 4 digits):')
init_bal=eval(input('Set the initial balance in your account: '))
acc1=Account(init_bal,acc_no)
print('\nCHOOSE THE TYPE OF TRANSACTION:')
print('\n1.CREDIT     2.DEBIT    3.BALANCE_ENQUIRY    4.LOCK')
print('\n\nEnter\n(C)for credit                  (D)for Debit\n(B)for Balance enquiry         (L)To LOCK')
print('\nINSTRUCTIONS:\n*Invalid option other than theese will results to LOCK the account!\n*Use CAPS only')
opt=input('\nChoose the required option:')
match opt:
       case "C":
                amt=eval(input('\nEnter the crediting amount:\n'))
                pin=eval(input('\nEnter the PIN: '))
                acc1.credit(amt, pin)                                                      
       case "D":
                amt=eval(input('Enter the debiting amount:\n'))
                pin=eval(input('\nEnter the PIN: '))
                acc1.debit(amt, pin)                 
       case "B":
                pin=eval(input('\nEnter the PIN: '))
                acc1.bal_enq(pin)                
       case "L":
                print('Account_no:',acc1.Account_number,'is locked successfully')
                print('\nThank you for using the service... ')   
       case _:
               print('CHOOSEN INVALID OPTION ACCOUNT LOCKED!')