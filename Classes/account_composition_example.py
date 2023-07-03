import random
import pdb
# from src.util.dbHelper import DBHelper # Example, we would import it

class DatabaseHelper:
    
    def __init__(self, dbAddress, username, password):
        self.connection = "I just connected"
    
    def writeDB(self):
        print("Writing....")
    
    def readDB(self):
        print("Reading....")

class AuthHelper:
    pass

# # Example of Inheritance
class AccountInheritance(DatabaseHelper):

    def __init__(self, userID, dbAddress, username, password, currency='USD'):
        super().__init__(dbAddress, username, password)
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
        self.writeDB()
        return random.randint(100, 1000)
    
    def __writeBalanceToDatabase(self):
        print("Saving to DB.")
        self.readDB()

# # Example of Composition
class AccountCoposition(object):

    def __init__(self, userID, dbAddress, username, password, currency='USD'):
        self.userID = userID
        self.currency = currency
        self.currentBalance = self.__readBalanceFromDatabase()
        print(f"Current balance is: {self.currentBalance}.")
        self.dbHelper = DatabaseHelper(dbAddress, username, password)
        self.auth = AuthHelper

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
        self.dbHelper.readDB()
        return random.randint(100, 1000)
    
    def __writeBalanceToDatabase(self):
        print("Saving to DB.")
        self.dbHelper.readDB()

pdb.set_trace()