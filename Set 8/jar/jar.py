class Jar:
    def __init__(self, capacity =12):
        self.cookies = 0
        if capacity >=0:
            self._capacity = capacity
        else:
            raise ValueError

    def __str__(self):
        return self.cookies * "🍪"

    def deposit(self, n):
        self.cookies = self.cookies + n
        if self.cookies > self._capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError
        else:
            self.cookies = self.cookies - n
            return self.cookies

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies


