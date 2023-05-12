class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def __str__(self):
        output = f"{self.name.center(30, '*')}\n"
        for i in self.ledger:
            if len(i['description']) < 23:
                description = i['description'].ljust(23)
            else:
                description = i['description'][:23]
            amount = f"{i['amount']:.2f}".rjust(7)
            output += f"{description}{amount}\n"
        output += f"Total: {sum(i['amount'] for i in self.ledger)}"
        return output

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def get_balance(self):
        return sum(i['amount'] for i in self.ledger)

    def check_funds(self, amount):
        return bool(self.get_balance() - amount >= 0)


def get_withdrawn(category):
    return abs(sum(
        float(i['amount']) for i in category.ledger if i['amount'] < 0
    ))

def get_precentage_spent(self, categories):
    totalWithdrawn = sum(get_withdrawn(i) for i in categories)
    precentageSpent = get_withdrawn(self) / totalWithdrawn
    return round(precentageSpent * 100)

def create_spend_chart(categories):
    longestName = len(max((i.name for i in categories), key=len))
    grid = [['   ' for i in range(10 + 1 + longestName)] for i in categories]

    for rowIndex, category in enumerate(categories):
        for i in range(10):
            if i <= get_precentage_spent(category, categories) / 10:
                grid[rowIndex][10 - i] = ' o '
            else:
                grid[rowIndex][10 - i] = '   '
        for count, value in enumerate(category.name):
            grid[rowIndex][11 + count] = f" {value} "

    yaxis = [f"{i}|".rjust(4, ' ') for i in range(100, -1, -10)]
    yaxis.extend(['    ' for i in range(longestName + 1)])
    xaxis = f"    {'---' * len(categories)}-"
    output = 'Percentage spent by category'

    for count, value in enumerate(i for i in zip(*grid)):
        output += '\n' + yaxis[count] + ''.join(value) + ' '
        if count == 10:
            output += '\n' + xaxis
    return output

