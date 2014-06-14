#Aaron Parker
#140614
#Cow Class

from Animal_Class import *

class Cow(Animal):
    """A cow"""
    #constructor
    def __init__(self,name):
        #calls parent class constructor with default values
        #growth rate = 2; food need = 6; water need = 3
        super().__init__(2,6,3,name)
        self._type = "Cow"

    #override grow method
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and food > self._food_need:
                self._weight += self._growth_rate * 2
            elif self._status == "Young" and food > self._food_need:
                self._weight += self._growth_rate *1.5
            elif self._status == "Old" and food == self._food_need:
                self._weight += self._growth_rate /2
            else:
                self._weight += self._growth_rate

        self._days_growing += 1

        self._update_status()

def main():
    #create new cow
    name = get_name()
    new_cow = Cow(name)
    print(new_cow.report())

    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == "__main__":
    main()
