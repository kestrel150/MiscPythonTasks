#Aaron Parker
#130614
#Potato Class

from Crop_class import *

class Potato(crop): #Potato is subclass of crop, inherits from crop
    """A potato crop"""

    #constructor
    def __init__(self):
        #call parent class constructor with default values for potato
        #growth rate = 1; light need = 3; water need; = 6
        super().__init__(1,3,6)
        self._type = "Potato"

def main():
    #create new potato crop
    potato_crop = Potato()
    print(potato_crop.report())

    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == "__main__":
    main()
    
