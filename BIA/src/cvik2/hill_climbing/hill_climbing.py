class Hill_climbing:
    def __init__(self, func):
        self.func = func

    def search(self, ranges):
        x1From, x1To, x2From, x2To = ranges
        
        self.func.visualize(x1From, x1To, x2From, x2To, [], [0, 0, 0])