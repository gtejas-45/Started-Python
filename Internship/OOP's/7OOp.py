# OOPs -->
# 1)Encapsulation - Wrapping up data into single entity , hiding the data and controlling the access

class BankAccount:

    def __init__(self):
        self.__balance = 5000 #in python we can't use the private variable like java so in python it uses ( __ )Dunder for private

    def show_balance(self):
        print(self.__balance)

account = BankAccount() 
# print(account.__balance) #if we directly access the balance it can't show because the access
account.show_balance()  #we access by the method 