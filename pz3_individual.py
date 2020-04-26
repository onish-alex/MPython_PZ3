import math

class Paralelogram:
    def __init__(self, firstSide, secondSide, diag):
        self.__firstSide = firstSide
        self.__secondSide = secondSide
        self.__diag = diag
    
    def getFirstSide(self): return self.__firstSide
    def setFirstSide(self, value): 
        if (self.__secondSide + self.__diag > value):
            self.__firstSide = value
        else:
            print("Incorrect value for first side!")
    def delFirstSide(self): del self.__firstSide
    
    def getSecondSide(self): return self.__secondSide
    def setSecondSide(self, value):
        if (self.__firstSide + self.__diag > value):
            self.__secondSide = value
        else:
            print("Incorrect value for second side!")
    def delSecondSide(self): del self.__secondSide
    
    def getDiag(self): return self.__diag
    def setDiag(self, value):
        if (self.__secondSide + self.__firstSide > value):
            self.__diag = value
        else:
            print("Incorrect value for diagonal!")
    def delDiag(self): del self.__diag

    firstSide = property(getFirstSide, setFirstSide, delFirstSide, "First Side")
    secondSide = property(getSecondSide, setSecondSide, delSecondSide, "Second Side")
    diag = property(getDiag, setDiag, delDiag, "Diagonal")

    def increase(self, n):
        self.firstSide = self.firstSide*n
        self.secondSide = self.secondSide*n
        self.diag = self.diag*n

    def decrease(self, n):
        self.firstSide = self.firstSide/n
        self.secondSide = self.secondSide/n
        self.diag = self.diag/n

    def __get_perimeter(self):
        return self.firstSide * 2 + self.secondSide * 2

    def __get_geron(self):
        return math.sqrt(self.__get_perimeter()/2 * (self.__get_perimeter()/2 - self.firstSide) * (self.__get_perimeter()/2 - self.secondSide) * (self.__get_perimeter()/2 - self.diag))
    
    def __get_square(self):
        return self.__get_geron() * 2
    
    def get_height(self):
        return self.__get_square() / self.secondSide
    
    def squareSqrt(self):
        return math.sqrt(self.__get_square())
    
    def perimeterSqrt(self):
        return math.sqrt(self.__get_perimeter())
    
    def get_anotherDiag(self):
        return math.sqrt(2*(pow(self.firstSide, 2) + pow(self.secondSide, 2)) - pow(self.diag, 2))
    
    def print_par(self):
        print("First: {}\nSecond: {}\nDiagonal: {}\n".format(self.firstSide, self.secondSide, self.diag))

par = Paralelogram(2, 3, 4)
par.print_par()
par.increase(2)
par.print_par()
par.decrease(1.6)
par.print_par()
print("sqrt of square: {}".format(par.squareSqrt()))
print("sqrt of perimeter: {}".format(par.perimeterSqrt()))
print("another diagonal: {}".format(par.get_anotherDiag()))
print("height: {}".format(par.get_height()))
