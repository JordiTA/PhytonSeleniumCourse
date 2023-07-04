import random
import pdb

class Account(object):

    def __init__(self, userID, currency='USD'):
        self.userID = userID
        self.currency = currency
        self.currentBalance = self.__readBalanceFromDatabase()
        print(f"Current balance is: {self.currentBalance}.")

    def withraw(self, ammount):
        self.currentBalance = self.currentBalance - float(ammount)
        print(f"New balance after withraw: {self.currentBalance}.")

    def deposit(self, ammount):
        self.currentBalance = self.currentBalance + float(ammount)
        print(f"New balance after deposit: {self.currentBalance}.")

    def generateStatement(self, startDate, endDate):
        pass

    def __readBalanceFromDatabase(self):
        print(f"Getting balance from db for {self.userID}.")
        return random.randint(100, 1000)

account = Account(9835)

pdb.set_trace()