from functools import reduce
import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        result = self.name.center(30, '*')
        result = reduce(
            lambda accum, item: accum
            + "\n"
            + item["description"][:23].ljust(23, ' ')
            + f"{item['amount']:.2f}"[:7].rjust(7, ' '),
            self.ledger,
            result
        )
        result += f"\nTotal: {self.get_balance()}"
        return result

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return reduce(lambda x, y: x+y['amount'], self.ledger, 0)

    def total_withdrawals(self):
        return reduce(lambda x, y: x+y["amount"] if y["amount"] < 0 else x, self.ledger, 0)

    def transfer(self, amount, to):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {to.name}")
            to.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True


def create_spend_chart(categories_list):
    result = "Percentage spent by category"
    total = reduce(lambda x, y: x+y.total_withdrawals(), categories_list, 0)
    names_percentages = list(map(lambda x:
                                 {"percentage": math.floor((x.total_withdrawals()/total*100) / 10)*10,
                                  "name": x.name},
                                 categories_list))
    for i in range(100, -10, -10):
        current_str = str(i).rjust(3, " ")+"| "
        for element in names_percentages:
            if (element["percentage"] < i):
                current_str += " "*1
            else:
                current_str += "o"
            current_str += " "*2
        result += f"\n{current_str}"
    result += "\n    -"+"---"*len(names_percentages)

    names_lengths = list(map(
        lambda x: {"name": x["name"], "length": len(x["name"])},
        names_percentages))
    maxNameLength = max(map(lambda x: x["length"], names_lengths))
    for i in range(0, maxNameLength):
        current_str = " "*5
        for element in names_lengths:
            if (element["length"] > i):
                current_str += element["name"][i]+" "*2
            else:
                current_str += " "*3
        result += "\n"+current_str

    return result
