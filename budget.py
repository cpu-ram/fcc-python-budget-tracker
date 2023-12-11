class Category:

    ledger=[]
    name=""
    def __init__(self, name):
        self.name=name

    def deposit(self, amount, description):
        self.ledger.add([amount, description])
    def withdraw(amount, description):
        pass
    def get_balance():
        balance=0
        for record in ledger:
            balance+=record[1]
    def transfer(to):
        pass
    def check_funds(amount):
        pass
def create_spend_chart():
    pass