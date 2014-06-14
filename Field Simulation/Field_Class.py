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

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"Crops": crop_report, "Animals": animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0

        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water need"]

        return {"Food":food,"Light":light,"Water":water}

    def grow(self,light,food,water):
        #grow crops (light and water available to all
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light,water)

        #grow animals (water available to all in same amounts
        #but food is total that must be shared
        if len(self._animals) > 0:
            food_required = 0
            #get total of food required
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["food need"]
            #if more food available than needed, extra is shared
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0
                
            #grow each animal
            for animal in self._animals:
                #get animals food needs
                needs = animal.needs()
                if food >= needs["food need"]:
                    #remove food for this animal from total
                    food -= needs["food need"]
                    feed = needs["food need"]
                    #additional food?
                    if additional_food > 0:
                        additional_food -= 1
                        #add to feed for animal
                        feed += 1
                #grow animal
                animal.grow(feed,water)
            

def display_crops(crop_list):
    print()
    print("The following crops are in this field:")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1

def display_animals(animal_list):
    print()
    print("The following animals are in this field:")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def select_crop_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop/animal: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop_animal(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_crop_animal(len(field._animals))
    return field.remove_animal(selected_animal)
    
def main():
    new_field = Field(5,2)
    
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())
    new_field.add_animal(Sheep("Shaun"))
    new_field.add_animal(Cow("Jim"))

    report = new_field.report_contents()
    print(report["Animals"])
    print()
    print(report["Crops"])
    
    report = new_field.report_needs()
    print(report)
    print()
    print()
    new_field.grow(10,10,7)
    print(new_field.report_contents())

    
if __name__ == "__main__":
    main()
