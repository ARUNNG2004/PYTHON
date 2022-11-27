class Father:
    def fishing(self):
        
        print("Fishing in river")

    def chess(self):
        print("Playing chess with Father")    
class Mother:
    def cooking(self):
        print("cooking in kitchen")

    def chess(self):
        print("Playing chess with Father")     
class Son(Father,Mother):
    def ride(self):
        print("Riding Bicycle")

o=Son()
o.ride()
o.fishing()
o.chess()