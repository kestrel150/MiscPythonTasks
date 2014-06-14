#Aaron Parker
#140614
#Sheep Class

from Animal_Class import *

class Sheep(Animal):
    """A sheep"""
    #constructor
    def __init__(self,name):
        #growth rate = 1, food need = 3 water need = 2
        super().__init__(1,3,2,name)
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby":
                self._weight += self._growth_rate * 3
            elif self._status == "Young":
                self._weight += self._growth_rate * 2
            elif self._status == "Old":
                self._weight += self._growth_rate / 4
            else:
                self._weight += self._growth_rate

        self._days_growing += 1
        self._update_status()

def main():
    #create new sheep
    name = get_name()
    new_sheep = Sheep(name)
    print(new_sheep.report())

    manual_grow(new_sheep)
    print(new_sheep.report())
    manual_grow(new_sheep)
    print(new_sheep.report())

if __name__ == "__main__":
    main()
