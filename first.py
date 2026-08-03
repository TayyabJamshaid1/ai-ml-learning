class Order:
     def __init__(self,amount):
          self.amount = amount


class OrderProcessor(Order):
        def process(self):
            print(f"Processing order of amount: {self.amount}")


o1=OrderProcessor(100)
o1.process()