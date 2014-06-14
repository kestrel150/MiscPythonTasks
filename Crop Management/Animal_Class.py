#Aaron Parker
#140614
#Animal Class

class Animal:
    """An animal"""
    #constructor
    def __init__(self, growth_rate, food_need, water_need, name):
        self._weight = 0 #represents growth
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Animal"
        self._name = name

    def needs(self):
        #returns dictionary with food and water needs
        return {'food need':self._food_need,'water need':self._water_need}

    def report(self):
        #returns dictionary with name, type, status, weight & days growing
        return {'name':self._name,'type':self._type,'status':self._status,'weight':self._weight,'days growing':self._days_growing}

    def _update_status(self):
        if self._weight > 10:
            self._status = "Old"
        elif self._weight > 5:
            self._status = "Adult"
        elif self._weight > 0:
            self._status = "Young"
        elif self._weight == 0:
            self._status = "Baby"
        
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate #adds growth rate to growth

        self._days_growing += 1

        self._update_status()

def main():
    new_animal = Animal(1,4,3, "Test")
    
    print(new_animal.report())
    print(new_animal.needs())
          
    new_animal.grow(4,3)

    print(new_animal.report())


if __name__ == "__main__":
    main()
