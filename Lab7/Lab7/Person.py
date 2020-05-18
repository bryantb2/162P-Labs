class Person: 
    # constructor
    def __init__(self, first_name = "", last_name="", address=""):
        self.first_name = first_name;
        self.last_name = last_name;
        self.address = address;

    # getters and setters
    def getFirstName(self):
        return self.first_name;
    def getLastName(self):
        return self.last_name;
    def getAddress(self):
        return self.address;
    def setFirstName(self, first_name):
        self.first_name = first_name;
    def setLastName(self, last_name):
        self.last_name = last_name;
    def setAddress(self, address):
        self.address = address;