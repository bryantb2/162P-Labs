
from Person import Person;

class CreditCard:
    # constructor
    def __init__(self, first_name = "", last_name = "", address = "", cc_number = 0, credit_limit = 0):
        self.owner = Person(first_name, last_name, address);
        self.credit_limit = credit_limit;
        self.cc_number = cc_number;
        self.balance = 0;

    # getters and setters
    def getBalance(self):
        return self.balance;
    def getCardNumber(self):
        return self.cc_number;
    def getOwnerName(self):
        return self.owner.getFirstName() +  ' ' + self.owner.getFirstName();
    def getAddress(self):
        return self.owner.getAddress();

    # methods
    def payBalance(self, payment_amount):
        if(payment_amount > 0):
            self.balance -= payment_amount;
            return True;
        return False;
    def makeCharge(self, charge_amount):
        if(charge_amount > 0):
            new_balance = self.balance + charge_amount;
            if(self.credit_limit >= new_balance):
                self.balance = new_balance;
                return True;
        return False;
    def setCreditLimit(self, new_limit):
        if(new_limit > 0):
            self.credit_limit = new_limit;
            return True;
        return False;
    