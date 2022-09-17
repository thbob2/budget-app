
class Category(object):
    
    def __init__(self,label):
        self.label = label
        self.ledger = []
    
    #* get_balance method that returns the current balance 
    #* of the budget category based on the deposits and withdrawals that have occurred.
    
    def get_balance(self):
        balance = 0
        balance += sum( float(item['amount']) for item in self.ledger)
        return balance

    #* check_funds method that accepts an amount as an argument.
    #* It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
    #* This method should be used by both the withdraw method and transfer method.

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False
    
    #* A deposit method that accepts an amount and description.
    #* If no description is given, it should default to an empty string.
    #* The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    
    def deposit(self,amount,description=""):
        self.ledger.append(
            {
                "amount":  amount,
                "description": description
            }
        )
        return True
    
     #* withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.
     #*If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
     
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": description
                }
            )
            return True
        return False         

    #* transfer method that accepts an amount and another budget category as arguments.
    #* The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
    #* The method should then add a deposit to the other budget category with the amount and the description 
    #* "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers.
    #* This method should return True if the transfer took place, and False otherwise.
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,"Transfer to {}".format(category.label))
            category.deposit(amount,"Transfer from {}".format(self.label))
            return True
        return False
    
    
    #* budget printe
    
    def __str__(self):
        
        ticket  = "" + self.label.center(30,"*") + "\n"
        for item in self.ledger:
            ticket += item['description'].ljust(23,' ')[:23]
            ticket += "{0:7.2f}".format(float(item['amount'])) + "\n"
            
        
        ticket += "Total: " + "{0:.2f}".format(float(self.get_balance()))
        
        return ticket
        
        
        

def create_spend_chart(categories):
    result = "Percentage spent by category\n"
    
    total_expenses  = max_lenth = 0
    
    expenses = []
    labels = []
    
    for category in categories:
        expense = sum(- item['amount'] for item in category.ledger if float(item['amount']) < 0)
        total_expenses += float(expense)
        
        
        
        max_lenth = max(len(category.label), max_lenth)
        expenses.append(expense)
        labels.append(category.label)
    
    expenses = [(float(item) / total_expenses)*100 for item in  expenses]
    labels = [label.ljust(max_lenth, " ") for label in labels]
    
    for index in range(100,-1,-10):
        result += str(index).rjust(3," ") + "|"
        
        for expense in expenses:
            result +=  " o " if expense >= index else "   "
        result += " \n"
        
    result += " "*4 + "---" * len(labels) +"-\n"
    
    for character in range(max_lenth):
        result += " "*4
        for label in labels:
            result +=  " " + label[character] + " "
        result += " \n"
    
    return result.strip("\n")
            