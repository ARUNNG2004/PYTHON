


class nokia:
    company="Nokia India"
    website="www.nokia-india.com"

    def contact_details(self):
        print("Address:cherry Road,Near Bus Stand,Salem")
class nokia11000(nokia):
    def __init__(self) -> None:
        self.name="Nokia 11000"
        self.year=1998        

    def product_details(self):
        print("Name   : ",self.name)
        print("Year   : ",self.year)
        print("Company   : ",self.company)
        print("Website   : ",self.website)

mobile=nokia11000()
mobile.product_details()
mobile.contact_details()