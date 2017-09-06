class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, item_status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.item_status = item_status


        self.tax = 1.15

    def sold(self):
        self.cost *= self.tax
        self.item_status = 'sold'
        print "--------------ITEM SOLD + tax-------------"
        return self


    def return_item(self):
        if self.item_status == 'opened':
            self.cost *= .8
            print "--------------ITEM returned/status",item_status," -------------"
        else: #do nothin
            print "no fee added"
        return self

    def display_info(self):
        print "Price",self.price
        print "Status:", self.item_status
        print "Item Name: ", self.item_name
        print "weight: ",self.weight
        print "Brand: ",self.brand
        print "Cost: ", self.cost

item1 = Product(10,'sugar',12,'nabisco',5,'for sale')
print "------------ item added ------------"
item1.display_info()

item2 = Product(12,'rice',2,'company',5,'for sale')
print "------------ item added ------------"
item2.display_info()

item1.sold()
print "------------ display info ------------"
item1.display_info()
print "------------ display info ------------"
item2.display_info()
print "------------ display info ------------"
item1.return_item()
print "------------ display info ------------"
item1.display_info()
