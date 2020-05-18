
from Car import Car

class Link:
    # constructor
    def __init__(self, car, next_car = None):
        self.car = car;
        self.next_car = next_car;

    # getters and setters
    def getCar(self):
        return self.car;
    def getNextCar(self):
        return self.next_car;


class CarList:
    # constructor
    def __init__(self):
        self.car_list = None;

    # methods
    def addCar(self, make = "", color = "", year = ""):
        new_car = Car(make, color, year);
        new_link = Link(new_car, self.car_list);
        self.car_list = new_link;

    def findCar(self, make = "", color = "", year = ""):
        new_car = Car(make, color, year);
        # loop through car list
        current_link = self.car_list;
        is_found = False;
        while(current_link != None):
            # compare and/or return
            if(current_link.getCar() == new_car):
                is_found = True;
            # go to next car
            current_link = current_link.next_car;
        return is_found;
    
    def removeHead(self):
        if(self.car_list != None):
            old_head = self.car_list.getCar();
            self.car_list = self.car_list.next_car;
            return old_head;
        return None;

    # operator overloads
    def __str__(self):
        display_string = '';
        current_link = self.car_list;
        while(current_link != None):
            display_string += str(current_link.getCar());
            display_string += '\n';
            current_link = current_link.next_car;
        return display_string;

    def __len__(self):
        length_count = 0;
        current_link = self.car_list;
        while(current_link != None):
            length_count += 1;
            current_link = current_link.next_car;
        return length_count;




