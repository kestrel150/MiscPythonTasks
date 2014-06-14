#Aaron Parker
#140614
#Field Class

from Potato_Class import *
from Wheat_Class import *
from Sheep_Class import *
from Cow_Class import *

class Field:
    """Simulate a field, containing animals and crops"""
    #constructor
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

def main():
    new_field = Field(5,2)
    print(new_field._crops)
    print(new_field._animals)
    print(new_field._max_animals)
    print(new_field._max_crops)

if __name__ == "__main__":
    main()
