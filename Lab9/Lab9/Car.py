
class Car:
    # constructor
    def __init__(self, car_make = "Ford", color = "Black", production_year = 1910):
        self.make = car_make;
        self.color = color;
        self.year = production_year;

    # getters and setters
    def getMake(self):
        return self.make;
    def getColor(self):
        return self.color;
    def getYear(self):
        return self.year;
    def setMake(self, make):
        self.make = make;
    def setColor(self, color):
        self.color = color;
    def setYear(self, production_year):
        self.year = production_year;

    # overloaded operators
    def __eq__(self, other):
        if(self.color == other.getColor() and 
           self.year == other.getYear() and
           self.make == other.getMake()):
            return True;
        return False;
    def __str__(self):
        return self.color + ' ' + str(self.year) + ' ' + self.make;
