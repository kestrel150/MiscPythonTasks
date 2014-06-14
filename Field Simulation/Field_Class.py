#Aaron Parker
#140614
#Field Class

import random

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
        #grow crops (light and water available to all)
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light,water)

        #grow animals (water available to all in same amounts
        #but food is total that must be shared)
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

def auto_grow(field,days):
    #grow field automatically over x days
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light,food,water)

def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1<= light <= 10:
                valid = True
            else:
                print("Value entered not valid [1-10]")
        except ValueError:
            print("Value entered not valid [1-10]")          
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1<= water <= 10:
                valid = True
            else:
                print("Value entered not valid [1-10]")
        except ValueError:
            print("Value entered not valid [1-10]")
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-100): "))
            if 1<= food <= 100:
                valid = True
            else:
                print("Value entered not valid [1-100]")
        except ValueError:
            print("Value entered not valid [1-100]")

    #grow field
    field.grow(light,food,water)
    

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

def display_crop_menu():
    print()
    print("Which crop type would you like to add?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. I don't want to add a crop - return me to the main menu")
    print()
    print("Please select an option from the above menu")

def display_animal_menu():
    print()
    print("Which animal type would you like to add?")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("0. I don't want to add an animal - return me to the main menu")
    print()
    print("Please select an option from the above menu")

def display_main_menu():
    print()
    print("1. Plant a new crop")
    print("2. Harvest a crop")
    print()
    print("3. Add an animal")
    print("4. Remove an animal")
    print()
    print("5. Grow field manually over 1 day")
    print("6. Grow field automatically over 30 days")
    print()
    print("7. Report field status")
    print()
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - potato not planted")
            print()
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - wheat not planted")
            print()

def add_animal_to_field(field):
    display_animal_menu()
    choice = get_menu_choice(0,2)
    name = get_name()
    if choice == 1:
        if field.add_animal(Cow(name)):
            print()
            print("Cow added")
            print()
        else:
            print()
            print("Field is full - Cow not added")
            print()
    elif choice == 2:
        if field.add_animal(Sheep(name)):
            print()
            print("Sheep added")
            print()
        else:
            print()
            print("Field is full - Sheep not added")
            print()

def manage_field(field):
    print("This is the field management program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        print()
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print("You removed the crop: {0}".format(removed_crop))
        elif option == 3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print("You removed the animal: {0}".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 6:
            auto_grow(field,30)
        elif option == 7:
            print(field.report_contents())
            print()
        elif option == 0:
            exit = True
            print()
    print("Thank you for using the field management program.")
    
    
def main():
    new_field = Field(5,2)
    manage_field(new_field)

    
if __name__ == "__main__":
    main()
