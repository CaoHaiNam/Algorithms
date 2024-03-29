import random

class RandomizedSet:

    def __init__(self):
        self.ls = []

    def insert(self, val: int) -> bool:
        if val in self.ls:
            return False
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.ls:
            self.ls.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.ls)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()