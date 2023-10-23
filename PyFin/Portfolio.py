
# Class created to model a portfolio for the purpose of simulating different strategies.

class Portfolio:
    def __init__(self, cash=10000, positions = {}):
        self.cash = cash
        self.positions = positions
        self.transactions = []
    
    # Used to INTIALIZE portfolio. Adds cash.
    def addCash(self, amount):
        self.cash = self.cash + amount
        return self.cash

    # Used to INTIALIZE portfolio. Subtracts cash.
    def subCash(self, amount):
        self.cash -= amount
        return self.cash

    # Used to INTIALIZE portfolio. Adds equities.
    def addEquity(self, positions = {}):
        for key, value in positions.items():
            if key in self.positions.keys():
                self.positions[key] += value
            else:
                self.positions[key] = value
        return self.positions

    # Used to INTIALIZE portfolio. Subtracts equities.
    def subEquity(self, positions = {}):
        for key, value in positions.items():
            if key in self.positions.keys():
                self.positions[key] -= value
            else:
                print("Error: Position does not exist in the portfolio.")
        return self.positions

    # Used in SIMULATION. Buys equities in a given stock.
    def buyEquity(self, ticker, shares, price, commission = 0):
        self.addEquity({ticker: shares})
        self.cash -= (shares * price + commission)

    # Used in SIMULATION. Sells equities in a given stock.
    def sellEquity(self, ticker, shares, price, commission = 0):
        pass

    # Used in SIMULATION. Shorts equities in a given stock.
    def shortEquity(self, ticker, shares, price, commission = 0):
        pass

    # Used in SIMULATION. Covers short equities in a given stock.
    def coverEquity(self, ticker, shares, price, commission = 0):
        pass

    # Returns sum of cash and current value of positions in portfolio.
    def currentEquity(self):
        currentEquity += self.cash
        for key, value in self.positions:
            #!!!!!!Figure out how to get price into this module!!!!!!
            currentEquity += self.positions.value(key) * price