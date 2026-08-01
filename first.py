class Order:
    def __init__(self,itemName,itemPrice):
        self.itemName=itemName
        self.itemPrice=itemPrice

    def showOrder(self):
        print(self.itemName," itemName with price ",self.itemPrice)

    def __gt__(self, other):
         if (self.itemPrice>other.itemPrice):
             return Order(self.itemName,self.itemPrice)
         elif (self.itemPrice<other.itemPrice):
             return Order(other.itemName,other.itemPrice)


o1=Order("Tea",78)
o1.showOrder()
o2=Order("Biscuit",58)
o2.showOrder()

o3=o1>o2
o3.showOrder()