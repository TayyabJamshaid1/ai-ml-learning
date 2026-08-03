class Order:
       def __init__(self,num1):
              self.num1=num1

       def show(self):
              print(self.num1)

       def __mul__(self,numInfo):
              num3=self.num1*numInfo.num1
              return Order(num3)


n1=Order(5)
n2=Order(7)
n3=n1*n2
n3.show()