"""
AUTHOR HARIN RAMJI
FILE IS AN EXAMPLE OF CLASS CREATION SPECIFICALLY ABOUT LIST WITH UNIQUE ENTRIES
"""
class Uniqueint(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e in self.vals:
            exit()
        else:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " is not in the list!!")

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ''
        return "( " + result[:-1] + " )"


s = Uniqueint
print(s)
s.insert(int(3))
