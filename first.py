class Student:
      college_name="Shalimar College"
      name="mehran"
      #parameterized Constructor
      def __init__(self,username,marks):
           self.name=username
           self.marks=marks

      
      def getAvgMarks(self):
          sum=0
          for i in self.marks:
              sum+=i
          avg=sum/300
          return avg
      
s1=Student("Usman",[34,45,33])
print(s1.getAvgMarks()) 
s1.name="Aleem" # again you can overide the name
