class GrandFather:
    def ownhouse(self):
        print("Grandpa House")


class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike ")

class Son(Father):
    def OwnBook(self):
        print("Son Have a Book")        


o=Son()
o.ownhouse()
o.ownBike()
o.OwnBook()