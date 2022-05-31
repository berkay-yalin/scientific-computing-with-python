from math import ceil, floor

class Category:
    def __init__(self, name):
        self.ledger = [] #[{'amount': x,'description': y}...]
        self.name = name

    def __str__(self):
        '''
        A title line of 30 characters where the name of the category is
        centered in a line of * characters.

        A list of the items in the ledger.
        Each line should show the description and amount.

        The amount should be right aligned, contain two decimal places, and
        display a maximum of 7 characters.

        A line displaying the category total.
        '''

        def format_title(name, asterisks):
            #asterisks represents number of * required to centre the name
            if isinstance(asterisks, float):
                return '*' * floor(asterisks) + name + '*' * ceil(asterisks)
            elif isinstance(asterisks, int):
                return '*' * asterisks + name + '*' * asterisks

        def format_ledger_items():
            ledgerDict = {i['amount']: i['description'] for i in self.ledger}
            ledgerStr = ''

            for k, v in ledgerDict.items():
                #format description
                if len(v) < 23:
                    description = v + ' ' * (23 - len(v))
                else:
                    description = v[:23]
                #format amount
                amount2dp = "{:.2f}".format(k)
                amount = ' ' * (7 - len(amount2dp)) + amount2dp
                #append to output string
                ledgerStr += description + amount + '\n'

            return ledgerStr

        def format_total():
            return sum([i['amount'] for i in self.ledger])

        ### PARENT FUNCTION ###
        title = format_title(self.name, (30 - len(self.name)) / 2)
        ledgerItems = format_ledger_items()
        total = f"Total: {format_total()}"
        return title + '\n' + ledgerItems + total

    def deposit(self, *args): #self, amount, description
        try:
            self.ledger.append({'amount':args[0],'description':args[1]})
        except:
            self.ledger.append({'amount':args[0],'description':''})

    def withdraw(self, *args): #self, amount, description
        if self.check_funds(args[0]):
            try:
                self.ledger.append({'amount':-args[0],'description':args[1]})
                return True
            except:
                self.ledger.append({'amount':-args[0],'description':''})
                return True
        else:
            return False

    def transfer(self, amt, obj): #self, amount transferred, category object
        if self.check_funds(amt):
            self.withdraw(amt, 'Transfer to ' + obj.name)
            obj.deposit(amt, 'Transfer from ' + self.name)
            return True
        else:
            return False

    def get_balance(self):
        return sum([i['amount'] for i in self.ledger])

    def check_funds(self, amount):
        return (True if self.get_balance() - amount >= 0 else False)

def create_spend_chart(categories):
    def get_precentage_spent(self):
        def get_withdrawn(self):
            #gets the total withdrawn of a single category
            all = [float(i['amount']) for i in self.ledger]
            withdrawn = list(filter(lambda x: x < 0, all))
            return abs(sum(withdrawn))

        totalWithdrawn = sum([get_withdrawn(i) for i in categories])
        precentageSpent = (get_withdrawn(self) / totalWithdrawn) * 100
        return floor(precentageSpent / 10) * 10 #round down to nearest 10

    ### PARENT FUNCTION ###
    categoryNames = [list(i.name) for i in categories]
    longestName = max(list(map(len, categoryNames)))

    grid = [['   ' for i in range(10 + 1 + longestName)] for i in categories]

    rowIndex = 0
    for category in categories:
        for i in range(10):
            if i <= get_precentage_spent(category) / 10: #if <= height of bar
                grid[rowIndex][10 - i] = ' o '
            else:
                grid[rowIndex][10 - i] = '   '

        for count, value in enumerate(category.name):
            grid[rowIndex][11 + count] = ' ' + value + ' '

        rowIndex += 1

    yaxis = [f'{i}|'.rjust(4, ' ') for i in range(100, -1, -10)]
    yaxis.extend(['    ' for i in range(longestName + 1)])
    xaxis = '    ' + '-' * 3 * len(categories) + '-'
    output = 'Percentage spent by category'

    for count, value in enumerate([list(i) for i in zip(*grid)]):
        if count != 10:
            output += '\n' + yaxis[count] + ''.join(value) + ' '
        else:
            output += '\n' + yaxis[count] + ''.join(value) + ' '
            output += '\n' + xaxis

    return output
