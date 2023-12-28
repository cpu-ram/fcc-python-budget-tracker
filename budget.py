from functools import reduce


class Category:

    ledger = []
    name = ""
    total = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        result = self.name.center(30, '*')
        result = reduce(
            lambda accum, item: accum
            + "\n"
            + item[description][:23].ljust(23, ' ')
            + str(round(item[amount], 2))[:7].rjust(7, ' '),
            self.ledger,
            result
        )
        result += f"\nTotal: {self.get_balance()}"
        return result

    def deposit(self, amount, description=""):
        self.ledger.add({"amount": amount, "description": description})

    def withdraw(self, amount, description):
        if this.check_funds(amount):
            self.ledger.add({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return reduce(lambda x, y: x+y[amount], ledger, 0)

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


def create_spend_chart(*args):
    result = ""
    total = reduce(lambda x, y: x+y.get_balance(), args, 0)
    names_percentages = map(lambda x:
                            {"amount": round(x.get_balance()/total*100, -1),
                             "name": x.name},
                            args).sort(lambda x: x[amount])
    for i in range(100, -10, -10):
        current_str = rjust(str(i), 3)+"| "
        for name in names_percentages:
            if (names_percentages[name] < i):
                current_str += " "*1
            else:
                current_str += "o"
            current_str += " "*2
            result += f"\n{current_str}"
    result += "    -"+"---"*len(names_percentages)

    names_lengths = names_percentages.map(
        lambda x: {"name": x[name], "length": len(x[name])})
    maxNameLength = max(names)
    for i in range(0, maxNameLength):
        current_str = " "*5
        for name, length in names_lengths:
            if (length > i):
                current_str += name[i]+" "*2
            else:
                current_str += " "*3
        result += current_str
