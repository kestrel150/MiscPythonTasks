from graphic_crop_item_class import *
from Potato_class import *

import field_resources

class PotatoGraphicsPixmapItem(CropGraphicsPixmapItem):
    """This class provides a graphical respresentation of a potato crop"""

    #constructor
    def __init__(self):
        self.available_graphics = [":/potato_seed.png",":/potato_seedling.png",
                                   ":/potato_young.png",":/potato_mature.png",
                                   ":/potato_old.png"]
        super().__init__(self.available_graphics)

        self.crop = Potato()
