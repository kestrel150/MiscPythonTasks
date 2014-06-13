#Aaron Parker
#130614
#Wheat Class

from Crop_Class import *

class Wheat(Crop):
    """A wheat crop"""

    #constructor
    def __init__(self):
        #growth rate = 2; light need = 5; water need; = 7
        super().__init__(2,5,7)
        self._type = "Wheat"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling":
                self._growth += self._growth_rate *1.5
            elif self._status == "Young":
                self._growth += self._growth_rate * 1.25
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


def main():
    #create new wheat crop
    wheat_crop = Wheat()
    print(wheat_crop.report())

    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
