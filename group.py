
class Group:
    def __init__(self):
        pass

    def Compose(self, one, other):
        pass

    def Inverse(self, item):
        pass

    def Identity(self):
        pass

    def Pow(self, item, exp):
        acc = self.Identity()
        for _ in range(exp):
            acc = self.Compose(acc, item)
        return acc

class ModPowGroup(Group):
    def __init__(self, prime):
        self.prime = prime
        super().__init__()
        pass

    def Compose(self, one, other):
        return (one*other) %self.prime
    
    def Inverse(self, item):
        return pow(item, -1, self.prime)
    
    def Identity(self):
        return 1