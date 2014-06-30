from graphic_animal_item_class import *
from Cow_class import *

import field_resources

class CowGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    """This class provides a graphical representation of a cow"""

    #constructor
    def __init__(self):

        self.available_graphics = [":/cow_baby.png",":/cow_poor.png",
                                   ":/cow_fine.png",":/cow_prime.png"]

        super().__init__(self.available_graphics)

        self.animal = Cow("")

