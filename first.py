class Person:
      def __init__(self,math,phy,chem):
            self.math=math
            self.phy=phy 
            self.chem=chem

      @property
      def percentage(self):
            return str(((self.math+self.phy+self.chem)/300)*100)+"%"

                  


p1=Person(18,25,66)
print(p1.percentage)
p1.math=99
print(p1.percentage)
#now the problem is you updated math score but still it is showing previous percentage instead of calculate again.This can be solved by two ways
