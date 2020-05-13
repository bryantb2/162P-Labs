
class Triangle:
    # class constructor
    def __init__(self, length1 = 0, length2 = 0, length3 = 0):
        default_length1 = 3;
        default_length2 = 4;
        default_length3 = 5;
        valid_triangle = False;
        if(length1 > 0 and length2 > 0 and length3 > 0):
            if(self.__is_valid_triangle(length1, length2, length3)):
                default_length1 = length1;
                default_length2 = length2;
                default_length3 = length3;
        self.sideLength1 = default_length1;
        self.sideLength2 = default_length2;
        self.sideLength3 = default_length3;

    # methods
    def isEquilateral(self):
        if(self.sideLength1 == self.sideLength2 
           and self.sideLength2 == self.sideLength3 
           and self.sideLength1 == self.sideLength3):
            return True;
        return False;

    def isScalene(self):
        if(self.sideLength1 != self.sideLength2 
           and self.sideLength2 != self.sideLength3 
           and self.sideLength1 != self.sideLength3):
            return True;
        return False;
    
    def isIsosceles(self):
        # counter equal length occurances
        are_equal_counter = 0;
        if(self.sideLength1 == self.sideLength2):
            are_equal_counter += 1;
        if(self.sideLength2 == self.sideLength3):
            are_equal_counter += 1;
        if(self.sideLength3 == self.sideLength1):
            are_equal_counter += 1;
        return True if are_equal_counter >= 1 else False;

    def isRight(self):
        # pythagorian theorum
        length1_squared = self.sideLength1**2;
        length2_squared = self.sideLength2**2;
        length3_squared = self.sideLength3**2;
        if(length1_squared + length2_squared != length3_squared):
            return False;
        elif(length3_squared - length1_squared != length2_squared):
            return False;
        elif(length3_squared - length2_squared != length1_squared):
            return False;
        else:
            return True;

    # getters and setters
    def getA(self):
        return self.sideLength1;
    def getB(self):
        return self.sideLength2;
    def getC(self):
        return self.sideLength3;
    def setA(self, length):
        self.sideLength1 = length;
    def setB(self, length):
        self.sideLength2 = length;
    def setC(self, length):
        self.sideLength3 = length;

    # validator function
    @staticmethod
    def __is_valid_triangle(length_a, length_b, length_c):
        # test for 3 equal lengths
        if(length_a == length_b and length_a == length_c and length_c == length_b):
            return True;
        # test for any other combination of lengths
        else: 
            if(length_a < length_b + length_c):
                return False;
            elif(length_b < length_a + length_c):
                return False;
            elif(length_c < length_a + length_b):
                return False;
            else:
                return True;