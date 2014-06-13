#Aaron Parker
#130613
#Crop Class

class Crop:
    """Generic food crop"""
    #constructor
    def __init__(self, growth_rate, light_need, water_need):

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        #above attributes prefixed with underscore to indicate
        #they should not be accessed directly from outside the class.

    def needs(self):
        #returns a dictionary containing light & water needs
        return {'light need':self._light_need,'water need':self._water_need}
        
    def report(self):
        #return a dictionary containing type, status, growth and days growing
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    def update_status():


    def grow():

        

def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs()['light need']) # can specify specific attribute to return by []
    print(new_crop.report())

if __name__ == "__main__":
    main()
        
