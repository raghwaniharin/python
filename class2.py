"""
AUTHOR HARIN RAMJI
FILE IS AN EXAMPLE OF CLASS CREATION SPECIFICALLY ABOUT FRACTIONS
"""
class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def getnum(self):
        return self.num

    def getdenom(self):
        return self.denom

    def __add__(self, other):
        newnum = other.getdenom() * self.getnum() + other.getnum() * self.getdenom()
        newdenom = other.getdenom() * self.getdenom()
        return Fraction(newnum, newdenom)

    def __sub__(self, other):
        newnum = other.getdenom()*self.getnum() - other.getnum()*self.getdenom()
        newdenom = other.getdenom * self.getdenom()
        return Fraction(newnum, newdenom)
    def convert(self):
        return self.getnum()/self.getdenom()


x = Fraction(3, 4)
y = Fraction(1, 2)
print(x)
print(x.getnum())
print(y)
print(Fraction.getdenom(y))
z = x+y
print(z)
print(Fraction.convert(z))
